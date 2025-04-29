import os
 
import requests
 
req_url = "https://api.quantum-computing.ibm.com/runtime/jobs?limit=10&offset=0&exclude_params=true"
 
headers_list = {
  "Accept": "application/json",
  "Authorization": f"Bearer {os.environ['IQP_API_TOKEN']}"
}
 
payload = ""
 
response = requests.request("GET", req_url, data=payload,  headers=headers_list)
 
print(response.json())