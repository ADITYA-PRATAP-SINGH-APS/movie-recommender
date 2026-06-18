import requests

url = "https://api.themoviedb.org/3/movie/19995?api_key=b8baa0c58d7209a5805e0b98ed653f0f&language=en-US"

try:
    response = requests.get(url, timeout=10)

    print("Status code:", response.status_code)
    print(response.text[:500])

except Exception as e:
    print(e)