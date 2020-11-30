from bs4 import BeautifulSoup
import requests

def gogo_convertor(episodes):
    res = ''
    for i in episodes :
        new_list = ''
        url = i 
        r = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data, 'html.parser')
        for link in soup.find_all('a'):
            new_link =  link.text
            if new_link[:8:] == "Download" :
                if link.get('href')[8:11:] == "cdn" :
                    print(link.get('href'))
                    new_list += link.get('href') + "\n"
        res += new_list
    return res