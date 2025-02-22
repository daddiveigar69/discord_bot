
import requests
from bs4 import BeautifulSoup

query='veigar'
url=f'https://lolalytics.com/lol/{query}/build/'


html_text=requests.get(url).text
soup=BeautifulSoup(html_text, 'lxml')
win_rate=soup.find('div', class_='mb-1 font-bold')
classes={'class_start':'mb-2 basis-full md:basis-1/3 lg:basis-1/6' , 'class_core':'basis-1/2 md:basis-1/3 lg:basis-auto', 'class_rest': 'mb-2 basis-1/2 md:basis-1/3 lg:basis-auto' }
#For starting items
print(classes['class_start'])
#For core items
print(classes['class_core'])
#For items 4 - 6
print(classes['class_rest'])
#pt restu foloseste un dictionar pt fiecare termen dif dintre clase si inlocuieste in clasa principal
'''n_items_p=soup.find_all('div', class_='class_needed')
n_items_c=n_items_p[0].select('[alt]')
print(n_items_p[0].next_element.text)   #shows the items order

print(n_items_c[0]['alt'])   #shows item name'''