import requests

# Download the correct Node.js icon
nodejs_url = 'https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-plain.svg'

try:
    response = requests.get(nodejs_url)
    if response.status_code == 200:
        with open('icons/nodejs.svg', 'wb') as f:
            f.write(response.content)
        print("Downloaded nodejs.svg")
except Exception as e:
    print(f"Error: {e}")