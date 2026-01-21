import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin


#for text extraction only 
testlink="https://www.w3schools.com/python/default.asp"
resp=requests.get(testlink)


print("Extracted data are:")
print(resp.text)




# for crawling and extracting links over a pages
url = "https://www.w3schools.com/python/pandas/default.asp"
response = requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")

links=set()
for tag in soup.find_all("a",href=True):  # having anchor tag for link on html
    full_url=urljoin(url,tag["href"])
    links.add(full_url)

for link in links:
 print(link)






# print(soup.title.text) # for extracting title




#extracting text and store in file
urllink="https://www.manjushreefinance.com.np/"

responsetext=requests.get(urllink)

print(responsetext.text)

newsoup=BeautifulSoup(responsetext.text,"html.parser") #parsed html tag, and newsoup will understand content on <p>hello</p> (tag) structure

with open("content.txt","w",encoding="utf-8") as f:  #using encoding="utf-8" it will extract all type of language from the content
   #f.write(responsetext.text) #it extract along with html tag as well
   f.write(newsoup.prettify()) #by prettify method of  beautiful soup, content will be extract more in prettier format , more user friendly
   #f.write(newsoup.get_text(separator="\n", strip=True)) #will

  #separator="\n" will add new line between text blocks for example helloram nepal will be
  #hello
  #ram nepal
   #strip=true means it remove extract space 



