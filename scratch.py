import requests

url = "https://runwayml.p.rapidapi.com/status"

querystring = {"uuid":"54503793-f04d-4448-840f-69ac254e30d1"}

headers = {
	"X-RapidAPI-Key": "d7ef3369e3msh49b877a74d19a78p16cce1jsnfc9162ec95d0",
	"X-RapidAPI-Host": "runwayml.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())