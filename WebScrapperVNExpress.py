import requests
from bs4 import BeautifulSoup
    
r = requests.get('https://e.vnexpress.net')

    # Parse HTML text
soup = BeautifulSoup(r.text, 'html.parser')
footer = soup.footer
data_set = []
footer_menu_list = footer.find_all('div', class_="col_menu_footer")
for list_footer in footer_menu_list:
    all_div = list_footer.find_all('div')
    for line in all_div:
            d = {'Menu':'', 'Link':''}
            try:
              d['Menu'] = line.text
              d['Link'] = line.a['href']
              data_set.append(d)
            except:
              print("error")
              continue
print(data_set)
print(len(data_set))