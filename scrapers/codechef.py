import requests
from bs4 import BeautifulSoup
import urllib3

class CodeChef:

    contests = {}
    url = ""

    def __init__(self):

        self.url = 'https://www.codechef.com/contests'

        self.contests = {
            "Code":[],
            "Name":[],
            "Start":[],
            "End":[]
        }
    
    def __scrape(self):

        page = requests.get(self.url)

        soup = BeautifulSoup(page.content,'html.parser')

        tables = soup.find_all('table')

        rows = tables[2].findAll('tr')

        for i in range(1,len(rows)):
            td = rows[i].findAll('td')
            self.contests["Code"].append(td[0].text)
            self.contests["Name"].append(td[1].text.replace("\n",""))
            self.contests["Start"].append(td[2].text)
            self.contests["End"].append(td[3].text)
    
    def getFutureContests(self):

        self.__scrape()
        return self.contests

if __name__ == "__main__":
    cc = CodeChef()
    print(cc.getFutureContests())
