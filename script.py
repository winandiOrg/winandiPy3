import requests

msg="hallo"

r = requests.get('https://coreyms.com')
print(r.status_code)
print(r.ok)
print(msg)
msg.