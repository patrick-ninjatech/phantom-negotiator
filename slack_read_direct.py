#!/usr/bin/env python3
"""Direct Slack API reader - bypasses S3 cache."""
import json, urllib.request, sys

def get_token():
    with open('/dev/shm/mcp-token') as f:
        content = f.read()
    tokens = {}
    for line in content.strip().split('\n'):
        if '=' in line:
            key, val = line.split('=', 1)
            tokens[key] = val
    return json.loads(tokens['Slack'])['bot_token']

def slack_api(method, params=None):
    token = get_token()
    url = f'https://slack.com/api/{method}'
    if params:
        url += '?' + '&'.join(f'{k}={v}' for k, v in params.items())
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}'})
    return json.loads(urllib.request.urlopen(req).read())

def read_channel(channel='C0AP92GANLA', limit=10):
    result = slack_api('conversations.history', {'channel': channel, 'limit': str(limit)})
    return result.get('messages', [])

def read_thread(channel='C0AP92GANLA', thread_ts=''):
    result = slack_api('conversations.replies', {'channel': channel, 'ts': thread_ts, 'limit': '50'})
    return result.get('messages', [])

def post_message(text, channel='C0AP92GANLA', thread_ts=None):
    token = get_token()
    payload = {'channel': channel, 'text': text}
    if thread_ts:
        payload['thread_ts'] = thread_ts
    data = json.dumps(payload).encode()
    req = urllib.request.Request(
        'https://slack.com/api/chat.postMessage',
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        data=data
    )
    return json.loads(urllib.request.urlopen(req).read())

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'thread':
        ts = sys.argv[2] if len(sys.argv) > 2 else ''
        msgs = read_thread(thread_ts=ts)
    else:
        limit = int(sys.argv[1]) if len(sys.argv) > 1 else 10
        msgs = read_channel(limit=limit)

    for m in msgs:
        user = m.get('user', m.get('bot_id', '?'))
        text = m.get('text', '')[:300]
        print(f'[{m["ts"]}] {user}: {text}')
        print()
