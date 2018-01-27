import requests

r = requests.get("localhost:5000")
print(r.text, "\n that was the text from localhost:5000")

resp = requests.get("localhost:5000/result")
print(r.text, "\n that was the text from localhost:5000/result")
