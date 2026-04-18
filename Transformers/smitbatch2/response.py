import requests

url = "https://memony49-transformer-on-flask.hf.space/analyze"

data = {
    "text": "the movie was not good"
}

response = requests.post(url, json=data)

print(response.json())