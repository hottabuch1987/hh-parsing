import requests
from bs4 import BeautifulSoup
from time import sleep



headers  = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',    
}



def get_url():
    for count in range(1, 2):  
        url = f'https://voronezh.hh.ru/search/vacancy?from=suggest_post&search_field=name&search_field=company_name&search_field=description&text=Django+django&enable_snippets=false&L_save_area=true&page={count}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('span', class_="serp-item__title-link-wrapper") 

        for d in data:  
            card_url =  d.find('a').get('href')
            yield card_url


def array():
    for card_url in get_url():
        print(card_url) 
        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', class_="bloko-column bloko-column_xs-4 bloko-column_s-8 bloko-column_m-12 bloko-column_l-10")     
        name = data.find('h1', class_='bloko-header-section-1').text
        price = data.find('span', class_='magritte-text___pbpft_3-0-4 magritte-text_style-primary___AQ7MW_3-0-4 magritte-text_typography-label-1-regular___pi3R-_3-0-4').text
        text = data.find('p', class_='vacancy-description-list-item').text

        yield name, price, text, card_url
