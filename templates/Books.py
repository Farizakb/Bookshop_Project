import sys
import requests
Film = sys.argv

x = ''
for  i in range(2, int(len(Film))):
    x =  x + f"{Film[i]} "



response = requests.get(f"https://www.omdbapi.com/?t={x}&apikey=ae705b48")
responses_js = response.json()
for key, value in responses_js.items():
    print(key, ":", value)


