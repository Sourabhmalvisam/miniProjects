import requests
from bs4 import BeautifulSoup as bs
user_name=input("Enter your Github Profile Username: ")
url="https://github.com/"+user_name
r=requests.get(url)
soup=bs(r.content,"html.parser")
profile_image=soup.find("img",{"alt":"Avatar"})["src"]
print(profile_image)