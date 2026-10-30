import requests

url = "https://clinicaltrials.gov/api/v2/studies?query.cond=diabetes&pageSize=1000"

response=requests.get(url)

with open("data/raw/trials.json","w") as file:
    file.write(response.text)

data=response.json()
print(len(data["studies"]))
