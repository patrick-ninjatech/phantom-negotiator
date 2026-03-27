# Phantom Memory

## Session History
- **2026-03-27**: Session started. Browser server running (Chrome 145, CDP on localhost:9222). Slack channel: #phantom-negotiator. Orchestrator running. Channel quiet — no pending requests. Resolved owner: Jason Sherman (jasonsherman736@gmail.com). Gmail session active.

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
- stage1 args: --slack-channel "#phantom-negotiator" --repo-name "phantom-negotiator"

## Owner
- **Name**: Jason Sherman
- **Email**: jasonsherman736@gmail.com
- **Phone**: 07548 375161
- **DOB**: March 27, 1995
- **Gmail**: Logged in, session active (verified 2026-03-27)

## Active Deals

### NYC Hotel May 24-31 — Status: Counter-Offers Sent / Awaiting Responses
- **Task**: Find best-priced hotels/Airbnb in NYC for May 24-31, 2026 (7 nights), email 50+ hotels
- **Vendor(s)**: 50 hotels emailed, 8 replied, 11 bounced, 5 counter-offers sent
- **Last action**: Sent counter-offers to 5 hotels (2026-03-27 ~15:30 UTC)
- **Awaiting**: Counter-offer responses from hotels
- **Outcome**: Pending — negotiating lower rates
- **Thread**: 1774624881.064469 (counter-offer thread)

**Replies + Counter-Offers (2026-03-27):**
1. **Pod 39/51** — Quoted: Bunk $220/nt, Full $241/nt, Queen $260/nt. Counter: Bunk $140/nt, Full $160/nt. Contact: Nick/Cristina, reservations@podhotel39.com
2. **Hotel Indigo Wall Street** — Quoted: $281/nt. Counter: $170/nt. Contact: Marissa P, FD@inwallst.com
3. **Hilton NY Times Square** — Quoted: King $309/nt, 2Q $359/nt. Counter: King $220/nt. Contact: Gary Prinz, NYCTS_HOTEL@hilton.com
4. **Sanctuary Hotel** — Quoted: $318/nt (15% off). Counter: $250/nt. Contact: Leni, reservations@sanctuaryhotelnyc.com
5. **Tempo by Hilton TS** — Quoted: $318/nt long-stay. Counter: $240/nt. Contact: Donielle Strawder, NYCTE_FO@hilton.com

**Other replies (no specific quote):**
6. TWA Hotel — book via website. Contact: Curlann John-Clark, cjohn-clark@twahotel.com
7. Motto by Hilton Chelsea — book via website. Contact: Marissa Panza, fdmottochelsea@hilton.com
8. Arthouse Hotel — special offers on website. Contact: AH-Reservations@arthousehotelnyc.com

**Bounced emails (11):** reservations@tryphotelnyc.com, reservations@elementtimessquare.com, info@cachetboutique.com, reservations@hotel46ts.com, info@hotelhaydennyc.com, EvelynRes@triumphny.com, reservations@thegallivantnyc.com, info@theradiohotel.com (+ 3 more)

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

## Known Sites
- **Airbnb NYC**: Only hotel listings available (no homes/rooms) due to Local Law 18
- **Google Hotels**: Good for price comparison, accepts date params via URL
- **Booking.com**: Redirects from direct search URLs — needs form interaction
- **Kayak**: Blocks automated access (CAPTCHA)
- **VRBO**: Blocks automated access (bot detection)
- **Gmail compose URL**: Most reliable method for bulk sending — `mail.google.com/mail/u/0/?view=cm&fs=1&to=X&su=Y&body=Z`
- **Gmail compose button**: `div[gh='cm']` or `text=Compose` — unreliable for rapid sequential sends
- **Gmail send button**: `div[aria-label='Send ‪(Ctrl-Enter)‬']` — works reliably
