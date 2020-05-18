import requests
import re


url = "https://ig.tools/api/creation_date.php"

username = str(input('Username : '))
payload = f"username={username}"
headers = {
    'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    'Accept-Language': "en-us",
    'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
    }

req= requests.post(url, data=payload, headers=headers)
res = req.text

date = re.search(r'<br> (.*\d?) to (.*\d?)', res)

print(f'{date[1]}:{date[2]}')
