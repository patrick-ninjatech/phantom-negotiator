#!/usr/bin/env python3
"""Send gardener emails via ProtonMail."""
from playwright.sync_api import sync_playwright
import time

def get_browser_ws():
    """Get the current browser WebSocket URL from CDP."""
    import json, urllib.request
    req = urllib.request.Request('http://[::1]:9222/json/version')
    resp = urllib.request.urlopen(req)
    ver = json.loads(resp.read())
    return ver['webSocketDebuggerUrl']

BROWSER_WS = get_browser_ws()
GARDEN_PHOTO = '/workspace/browser-automation/garden_photo.png'

SUBJECT = 'Garden Cleanup Quote Request \u2014 London'
BODY_LINES = [
    "Hi,",
    "",
    "I hope this email finds you well. I'm looking for a professional gardener to help with a garden cleanup at my property in London.",
    "",
    "The garden has become quite overgrown and needs a thorough clearance \u2014 including cutting back overgrown shrubs and hedges, clearing weeds and debris, tidying up the lawn area, and general garden maintenance to bring it back to a presentable state.",
    "",
    "I've attached a photo of the garden so you can see the current condition. Could you please provide a quote for the cleanup work? I'm flexible on timing and happy to discuss the scope further.",
    "",
    "Looking forward to hearing from you.",
    "",
    "Best regards,",
    "Anthony Santiago"
]

GARDENERS = [
    ("City Gardeners", "info@citygardeners.co.uk"),
    ("Urban Gardeners", "office@urbangardeners.co.uk"),
    ("Green Dream London", "office@greendreamlondon.co.uk"),
    ("Ace Maintenance", "info@acemaintenance.co.uk"),
    ("Just Clear", "hello@justclear.com"),
    ("The Urban Gardeners", "toby@theurbangardeners.co.uk"),
    ("Professional Gardening Services", "professionalgardening2016@gmail.com"),
    ("Urban Bloom Gardening", "hello@urbanbloomgardening.co.uk"),
    ("Master Landscapers", "office@masterlandscapers.co.uk"),
    ("Freddie's Gardening", "office@freddiesgardening.co.uk"),
    ("Tidy Properties", "office@tidyproperties.co.uk"),
]


def close_all_composers(page):
    """Close all open compose windows."""
    for _ in range(15):
        close_btns = page.locator('[data-testid="composer:close-button"]')
        if close_btns.count() > 0:
            close_btns.first.click()
            time.sleep(0.5)
            try:
                page.click('button:has-text("Delete")', timeout=2000)
                time.sleep(0.5)
            except Exception:
                try:
                    page.click('button:has-text("Discard")', timeout=1000)
                    time.sleep(0.5)
                except Exception:
                    pass
        else:
            break
    time.sleep(1)


def send_email(page, name, email, step):
    """Send a single email via ProtonMail compose."""
    print(f"\n--- [{step}/{len(GARDENERS)}] {name} ({email}) ---")

    # Click New message
    page.click('[data-testid="sidebar:compose"]')
    time.sleep(2)

    # Fill To field
    to_input = page.locator('[data-testid="composer:to"]').last
    to_input.click()
    to_input.fill(email)
    time.sleep(0.5)
    to_input.press('Enter')
    time.sleep(1)

    # Fill Subject
    subj_input = page.locator('[data-testid="composer:subject"]').last
    subj_input.fill(SUBJECT)
    time.sleep(0.5)

    # Fill Body via iframe
    iframe_locator = page.locator('[data-testid="rooster-iframe"]').last
    frame = iframe_locator.content_frame
    body_div = frame.locator('div[contenteditable="true"]').first
    body_div.click()
    time.sleep(0.3)

    # Select all and delete existing content
    page.keyboard.press('Control+a')
    time.sleep(0.1)
    page.keyboard.press('Delete')
    time.sleep(0.3)

    # Type body line by line
    for i, line in enumerate(BODY_LINES):
        if line:
            page.keyboard.type(line, delay=2)
        if i < len(BODY_LINES) - 1:
            page.keyboard.press('Enter')
        time.sleep(0.05)

    time.sleep(1)

    # Attach garden photo
    file_input = page.locator('[data-testid="composer-attachments-button"]').last
    file_input.set_input_files(GARDEN_PHOTO)
    print("  Attaching photo...")
    time.sleep(2)

    # Handle "Insert image" dialog — click "Attachment" button
    try:
        attach_btn = page.locator('button:has-text("Attachment")').first
        if attach_btn.is_visible(timeout=5000):
            attach_btn.click()
            print("  Clicked 'Attachment' in image dialog")
            time.sleep(1)
    except Exception:
        pass  # Dialog may not appear

    time.sleep(6)  # Wait for upload to complete

    # Screenshot before sending
    page.screenshot(path=f'phantom/screenshots/email_{step}.png')

    # Click Send
    page.locator('[data-testid="composer:send-button"]').last.click()
    time.sleep(4)

    print(f"  SENT!")
    time.sleep(3)


def main():
    pw = sync_playwright().start()
    browser = pw.chromium.connect_over_cdp(BROWSER_WS)
    ctx = browser.contexts[0]
    page = None
    for p in ctx.pages:
        if 'proton' in p.url.lower():
            page = p
            break

    if not page:
        print("ERROR: No ProtonMail page found")
        browser.close()
        pw.stop()
        return

    print(f"Connected: {page.url}")

    # Close any open compose windows
    close_all_composers(page)
    remaining = page.locator('[data-testid="composer:close-button"]').count()
    print(f"Compose windows cleared. Remaining: {remaining}")

    sent_count = 0
    errors = []

    for i, (name, email) in enumerate(GARDENERS, 1):
        try:
            send_email(page, name, email, i)
            sent_count += 1
            print(f"  Progress: {sent_count}/{len(GARDENERS)}")
        except Exception as e:
            error_msg = f"{name} ({email}): {str(e)[:150]}"
            errors.append(error_msg)
            print(f"  ERROR: {error_msg}")

            # Close the compose window
            try:
                page.locator('[data-testid="composer:close-button"]').last.click()
                time.sleep(1)
                try:
                    page.click('button:has-text("Delete")', timeout=2000)
                except Exception:
                    try:
                        page.click('button:has-text("Discard")', timeout=1000)
                    except Exception:
                        pass
            except Exception:
                pass
            time.sleep(2)

    print(f"\n=== RESULTS ===")
    print(f"Sent: {sent_count}/{len(GARDENERS)}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    page.screenshot(path='phantom/screenshots/email_final.png')
    browser.close()
    pw.stop()


if __name__ == '__main__':
    main()
