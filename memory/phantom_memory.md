# Phantom Memory

## Session History
- **2026-03-27**: Session started. Browser server running (Chrome 145, CDP on localhost:9222). Slack channel: #phantom-negotiator. Orchestrator running. Channel quiet — no pending requests. Standing by.

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
- **Name**: Unknown — resolve via Gmail profile or ask user on first negotiation task

## Active Deals
_(none yet)_

## Known Sites
