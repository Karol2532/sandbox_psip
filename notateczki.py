import requests

miasto = "zamosc"

url = f"https://danepubliczne.imgw.pl/api/data/synop/station/{miasto}"

response = requests.get(url)

print(response.json())
