  
import requests
headers = {
  "Content-type": "Application/json"
  }

f = open('data.json','w+')
data = requests.get("https://corona-api.com/timeline",headers=headers).json()
f.write(str(data))
f.close()
