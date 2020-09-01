#!/usr/bin/python3
import requests, re, argparse, json

# Parsing arguments.
parser = argparse.ArgumentParser()

# Adding arguments.
parser.add_argument("username", help="Instagram username", metavar="USERNAME")

# Read arguments from command line.
args = parser.parse_args()

# URL to prepare for POST request
url = "https://www.instagram.com/accounts/account_recovery_send_ajax/"

g = requests.get("https://www.instagram.com/accounts/password/reset/").text # get request to get the csrftoken data variable
token = re.search(r'csrf_token":"(.*?)"',g).group(1) # csrftoken fetcher

# headers 
headers = {'x-csrftoken': token}

data = {'email_or_username': args.username, 'recaptcha_challenge_field':''}

def main():
	r = requests.post(url, data=data, headers=headers)
	a = json.loads(r.text)
	if a['status'] == "fail":
		print(f"[-] Status: {a['status']}")
		print(f"[-] Response: {a['message']}")
	else:
		print(f"[+] Status: {a['status']}")
		print(f"[+] Response: {a['message']}")
	print("\n~ valentine")

if __name__ == "__main__":
	main()