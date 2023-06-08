import requests
from bs4 import BeautifulSoup as bs

URL = 'https://www.geeksforgeeks.org/page/'

for page in range(1, 10):
    req = requests.get(URL + str(page) + '/')
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})

    for i in range(4, 19):
        if i < len(titles):
            if page > 1:
                print(f"{(i-3)+page*15}" + titles[i].text)
            else:
                print(f"{i-3}" + titles[i].text)
        else:
            break  # Exit the loop if index i is out of range
