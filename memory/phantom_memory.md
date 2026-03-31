# Phantom Memory

## Session History
- **2026-03-27**: Session started. Hotel negotiation task completed — 50 hotels emailed, 12 replied, 5 counter-offers sent, all declined or no response. Comparison report delivered. Awaiting Jason's booking decision.
- **2026-03-28**: Monitoring continues. No new hotel replies or Slack messages. 3 counter-offers marked as no-response. Deal effectively complete. Gmail session expired (~08:30 UTC) — Google requires reCAPTCHA re-auth. Notified Jason on Slack. Jason needs to re-login via VNC/noVNC to restore Gmail access.
- **2026-03-29**: Idle monitoring most of day. Jason asked for session summary (~21:00 UTC) — posted full summary to Slack thread. Gmail still expired. All tasks complete — awaiting next instruction.
- **2026-03-30**: Continued monitoring. No new messages from Jason after session summary. Idle.
- **2026-03-31**: Jason requested continuation of gardener task. Posted VNC URL for ProtonMail login. Downloaded garden photo (3.9MB). Email template prepared for 11 London gardeners. Waiting for Jason to log in.

## Configuration
- **Slack channel**: #phantom-negotiator (ID: C0AP92GANLA)
- **GitHub repo**: patrick-ninjatech/phantom-negotiator
- **Branch**: status-update-from-phantom
- **Workspace**: /workspace/browser-automation
- **Agent**: Phantom (Browser Automation Agent)
- **Browser**: Chrome/145.0.7632.6, CDP on localhost:9222
- **VNC**: port 5901 (no password, -nopw flag active)
- **noVNC**: port 6080
- **Dashboard**: port 9000

## Deployment Notes
- VNC password auth is disabled (`-nopw`) — vnc_setup autostart=false in supervisord
- Git remote set to: https://github.com/patrick-ninjatech/phantom-negotiator.git
- GITHUB_TOKEN must be set from /dev/shm/mcp-token before git_auto_commit.sh runs
- git remote must be set with x-access-token before auto-commit (done in WAKE UP sequence)
- ⚠️ git_auto_commit.sh CORRUPTS remote URL — always run `git remote set-url origin "https://github.com/patrick-ninjatech/phantom-negotiator.git" && gh auth setup-git` after it runs
- stage1 args: --slack-channel "#phantom-negotiator" --repo-name "phantom-negotiator"

## Owner
- **Name**: Jason Sherman
- **Email**: jasonsherman736@gmail.com
- **Phone**: 07548 375161
- **DOB**: March 27, 1995
- **Gmail**: ⚠️ SESSION EXPIRED (2026-03-28 ~08:30 UTC) — needs manual re-login via VNC

## Active Deals

### NYC Hotel May 24-31 — Status: Complete (Awaiting Jason's Booking Decision)
- **Task**: Find best-priced hotels/Airbnb in NYC for May 24-31, 2026 (7 nights), email 50+ hotels
- **Vendor(s)**: 50 hotels emailed, 12 replied, 11 bounced, 5 counter-offers sent, 2 declined, 3 no response
- **Last action**: Posted full comparison report to Slack (2026-03-27 ~16:00 UTC)
- **Awaiting**: Jason's booking decision only (counter-offers exhausted)
- **Outcome**: Hotels won't negotiate for May (busy season). Best bet is online booking via Google Hotels/OTAs.
- **Thread**: 1774620193.516509 (main thread)

**Counter-Offer Results:**
1. **Pod 39/51** — ❌ Declined. Firm at $220/nt all-in. Google: $95-120/nt before tax.
2. **Hotel Indigo Wall Street** — ❌ Declined. Firm at $281/nt. "May is very busy." Google: $166/nt.
3. **Hilton NY Times Square** — ❌ No response to counter. Quoted $309/nt King. Counter: $220/nt. Google: $185/nt.
4. **Sanctuary Hotel** — ❌ No response to counter. Quoted $318/nt. Counter: $250/nt. Google: $146/nt.
5. **Tempo by Hilton TS** — ❌ No response to counter. Quoted $318/nt. Counter: $240/nt. Google: $325/nt.

**Best options (book online):**
- Pod 51: $95/nt + tax (~$770 total) — cheapest
- Hampton Inn TS Central: $128/nt + tax (~$1,030 total) — best TS value
- Motto by Hilton Chelsea: $148/nt + tax (~$1,190 total) — trendy, 4.5 stars

**Lessons learned:** NYC hotels don't negotiate much for May. Email quotes were higher than OTA prices. Direct booking benefits = flexibility, not price.

**Shortlist (per night / 7-night total):**
1. Pod 51 (Midtown) — $103/night (~$721) ⭐4.1 — 37% below usual
2. Pod 39 (Murray Hill) — $198/night (~$1,384) ⭐4.7
3. Holiday Inn Express Brooklyn Sunset Park — $158/night (~$1,106) ⭐4.0
4. The Manhattan at Times Square — $162/night (~$1,134) ⭐3.0
5. Renaissance NY Harlem — $164/night (~$1,148) ⭐3.6
6. Washington Hotel NYC — $171/night (~$1,197) ⭐3.7
7. Hilton Garden Inn FiDi — $177/night (~$1,239) ⭐4.3
8. Radio Hotel (Washington Heights) — $181/night (~$1,269 via Airbnb) ⭐4.5
9. Hilton NY Times Square — $195/night (~$1,365) ⭐4.1

**Notes:**
- Airbnb has NO apartment/room listings in NYC (Local Law 18 restrictions) — hotels only
- VRBO/Kayak blocked by bot detection
- May is shoulder season — prices moderate, negotiation possible
- Week-long stays can often get 10-20% off via direct booking/email

### London Garden Cleanup — Status: In Progress (Awaiting ProtonMail Login)
- **Task**: Email 11 London gardeners for cleanup quotes, negotiate best price
- **Email**: anthony.santiago76@proton.me (Proton Mail — signing as Anthony Santiago)
- **Garden photo**: /workspace/browser-automation/garden_photo.png
- **Email template**: /workspace/browser-automation/gardener_email_template.txt
- **Thread**: 1774872562.843209 (original), 1774952800.002219 (continuation)
- **Status**: Jason approved list ("proceed") on 2026-03-30 but emails weren't sent. Resuming 2026-03-31.
- **Gardener list (approved)**:
  1. City Gardeners (North London) — info@citygardeners.co.uk
  2. Urban Gardeners (SE London) — office@urbangardeners.co.uk
  3. Green Dream London (East London) — office@greendreamlondon.co.uk
  4. Ace Maintenance (London-wide) — info@acemaintenance.co.uk
  5. Just Clear (Garden clearance) — hello@justclear.com
  6. The Urban Gardeners (SW London) — toby@theurbangardeners.co.uk
  7. Professional Gardening Services (London) — professionalgardening2016@gmail.com
  8. Urban Bloom Gardening (London) — hello@urbanbloomgardening.co.uk
  9. Master Landscapers (N/E London) — office@masterlandscapers.co.uk
  10. Freddie's Gardening (London) — office@freddiesgardening.co.uk
  11. Tidy Properties (London) — office@tidyproperties.co.uk

## Known Sites
- **Airbnb NYC**: Only hotel listings available (no homes/rooms) due to Local Law 18
- **Google Hotels**: Good for price comparison, accepts date params via URL
- **Booking.com**: Redirects from direct search URLs — needs form interaction
- **Kayak**: Blocks automated access (CAPTCHA)
- **VRBO**: Blocks automated access (bot detection)
- **Gmail compose URL**: Most reliable method for bulk sending — `mail.google.com/mail/u/0/?view=cm&fs=1&to=X&su=Y&body=Z`
- **Gmail compose button**: `div[gh='cm']` or `text=Compose` — unreliable for rapid sequential sends
- **Gmail send button**: `div[aria-label='Send ‪(Ctrl-Enter)‬']` — works reliably
- **Proton Mail**: mail.proton.me — Login page at account.proton.me/mail. Need to explore compose UI once logged in.
- **slack_interface.py read**: Uses S3 cache, often empty. Use slack_read_direct.py for reliable reads.
