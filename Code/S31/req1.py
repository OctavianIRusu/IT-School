import requests
import time

POSTS_URL = "https://jsonplaceholder.typicode.com/posts"
URL = "https://jsonplaceholder.typicode.com/comments"    

def get_with_retry(url):
    try:
        resp = requests.get(url, timeout=(3.5, 30))
    except requests.ReadTimeout:
        print("Connection timed out. Retrying after 3 seconds.")
        time.sleep(3)
        get_with_retry(url)
    else:
        resp.raise_for_status()
        return resp.json()

try:
    get_with_retry(URL)
except requests.RequestException as err:
    print(err)