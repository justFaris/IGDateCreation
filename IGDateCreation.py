import requests
import re
import threading


def check(user):
       try:
           url = "https://ig.tools/api/creation_date.php"
           payload = f"username={user}"
           headers = {
           'User-Agent': "Cookieizi/1.0",
           'Accept-Language': "en-us",
           'Content-Type': "application/x-www-form-urlencoded; charset=UTF-8"
           }
           req= requests.post(url, data=payload, headers=headers)
           res = req.text
           date = re.search(r'<br> (.*\d?)', res)
           print(f'</> {user}: {date[1]}')
       except:
            print(f"</> {user}: Sorry, this page isn't available.")
   

for user in open("usernames.txt",'r').read().splitlines():
    threadss = threading.Thread(target= check(user))
    threadss.start()

