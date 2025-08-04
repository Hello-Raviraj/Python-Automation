import requests

url = "http://testphp.vulnweb.com/login.php"
data = {
    "uname": "test",  # username
    "pass": "test"    # password
}

headers = {
    "User-Agent": "Mozilla/5.0"  # mimic a real browser
}

# Start a session to handle cookies
session = requests.Session()
response = session.post(url, data=data, headers=headers)

# Check if successful
if "Logout" in response.text or "logout" in response.text:
    print("✅ Login successful!")
else:
    print("❌ Login failed.")

# Optional: print final URL or page preview
print("Final URL:", response.url)
print("Preview:\n", response.text[:300])
