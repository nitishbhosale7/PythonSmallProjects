
import time
import requests
baseurl = "https://api.dictionaryapi.dev/api/v2/entries/en/"
print("Hello Welcome to the Dictionary Created By Nitish")

time.sleep(3)
while(True):
    search = input("Enter the word you want to search = ")
    if(search):
        break

try:
    final = baseurl + search.lower()
    r = requests.get(final)

    data = r.json()
    data1 = data[0]
    print("Meaning -- ")
    print("\t \t" +data1['meanings'][0]['definitions'][0]['definition'])

except Exception:
    print("sorry could not found that word")



