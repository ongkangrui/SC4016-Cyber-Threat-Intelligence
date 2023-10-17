import requests

url = "http://noescapemsqxvizdxyl7f7rmg5cdjwp33pg2wpmiaaibilb4btwzttad.onion/"
authurl = "http://noescapemsqxvizdxyl7f7rmg5cdjwp33pg2wpmiaaibilb4btwzttad.onion/c9cc21dcd195ed51/f0a89ce8cbaea9b0/auth"
posturl = "http://noescapemsqxvizdxyl7f7rmg5cdjwp33pg2wpmiaaibilb4btwzttad.onion/c9cc21dcd195ed51/f0a89ce8cbaea9b0/posts"

# creates a new session
session = requests.Session()
session.proxies = {'http':  'socks5h://127.0.0.1:9150', 
                   'https': 'socks5h://127.0.0.1:9150'}

# POST request for authenthication
header = {'Content-Type': 'application/json', 'Verify':'EsaymapRTc9JbqTHYcppgAJ8xHbX4Dxb'}
page = session.post(authurl,headers=header, data={})
token = page.text

# POST request to get json data from site
header = {'Content-Type': 'application/json', 'Verify':'EsaymapRTc9JbqTHYcppgAJ8xHbX4Dxb', 'token':token}
page = session.post(posturl, headers = header, data={})
data = page.json()

