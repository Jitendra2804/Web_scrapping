import requests
from bs4 import BeautifulSoup as bs

URLs = ['https://www.geeksforgeeks.org', 'https://www.geeksforgeeks.org/page/10/']

for url in URLs:
    req = requests.get(url)
    soup = bs(req.text, 'html.parser')

    titles = soup.find_all('div', attrs={'class', 'head'})
    for i in range(4, 19):
        if len(titles) > i:
            if url != URLs[0]:
                print(f"{(i - 3) + (URLs.index(url) * 15)}" + titles[i].text)
            else:
                print(f"{i - 3}" + titles[i].text)
        else:
            break  # Exit the loop if index i is out of range
