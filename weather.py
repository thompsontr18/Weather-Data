from bs4 import BeautifulSoup
import requests
import colorama
from colorama import Fore
import time
import pathlib
from pathlib import Path


statelist = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga', 'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']
while True:
	state = input("> Enter your state abbreviation: ")
	if state.lower() in statelist:
		break

city = input("> Enter your city: ")
url = "https://www.wunderground.com/weather/us/"+state+"/"+city


DICT = pathlib.Path(__file__).parent / "𝙛𝙞𝙡𝙚𝙣𝙖𝙢𝙚"

cities = {
	word.title()
	for word in Path(DICT).read_text().splitlines()
}

if city.title() not in cities:
	print("❌❌❌ ERROR ❌❌❌\n" + Fore.RED + city.title()+ " is not a valid city in the United States. Rerun your program and enter a valid city.")
	quit()

html = requests.get(url)
soup = BeautifulSoup(html.text, "html.parser")
hi = soup.findAll("span", attrs={"class":"hi"})
lo = soup.findAll("span", attrs={"class":"lo"})
temp = soup.findAll("span", attrs={"class":"wu-value wu-value-to"})


#quits if user inputted a city that is not in the state they entered
for test in lo:
	if "--" in test.text:
		print("❌❌❌ ERROR ❌❌❌\n" + Fore.RED + city.title()+", "+state.upper()+" is not a valid location. Maybe you meant a different city/state? Rerun your program and enter a valid city.")
		quit()

print(">")
time.sleep(1)
print("> Getting weather data for " +city.title()+", "+state.upper())
time.sleep(1)
print('>')
time.sleep(1)
print('>')
time.sleep(1)

print("Current Temperature: "+temp[0].text+"°F")
for l in lo:
	print("Low/High: " + Fore.BLUE +l.text+"F", end = "")

for h in hi:
	print(Fore.WHITE + "/" + Fore.RED + h.text+"F")
