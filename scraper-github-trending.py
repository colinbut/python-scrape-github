import requests
from bs4 import BeautifulSoup
page = requests.get('http://github.com/trending')
#print(page)

soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)

#repo = soup.find(class_="Box")
repo_list = soup.find_all(class_="Box-row")
#print(len(repo_list))

print('Developer, Repo, Stars, Forks')
for repo in repo_list:
    full_repo_name = repo.find(class_='h3 lh-condensed').find('a')['href'][1:].split('/')
    stars = repo.find(class_='octicon octicon-star').parent.text.strip()
    forks = repo.find(class_='octicon octicon-repo-forked').parent.text.strip()
    
    #print(full_repo_name)
    developer = full_repo_name[0].strip()
    repo_name = full_repo_name[1].strip()

    print(developer + ',' + repo_name + ',' + stars + ',' + forks)