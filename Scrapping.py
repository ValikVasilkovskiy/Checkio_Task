# TODO
# 1. write to file inside while loop
# 2. Get detailed info
# 3. create separete functions for each subparser
from time import sleep
from random import randint
import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent


def random_sleep(start=1, end=3):
    sleep(randint(start, end))


BASE_URL = 'https://www.work.ua'
DNIPRO_PATH = '/jobs/'
PAGE = 1
RESULT = {}
START_URL = BASE_URL + DNIPRO_PATH

print("START")
while True:
    print("PAGE: {}".format(PAGE))
    print('sleeping')
    random_sleep()
    headers = {'User-Agent': generate_user_agent()}
    payload = {'page': PAGE}
    response = requests.get(START_URL, params=payload, headers=headers)
    assert response.status_code == 200
    soup = BeautifulSoup(response.text, 'html.parser')
    cards = soup.find_all(
        "div",
        class_="card card-hover card-visited wordwrap job-link",
    )
    if not cards:
        break

    for card in cards:
        card_a = card.find('h2').find('a')
        RESULT[card_a['href']] = card_a.text
        # I would start here
        # random_sleep()
        # response = requests.get(BASE_URL + card_a['href'], headers=headers)
        # soup_2 = BeautifulSoup(response.text, 'html.parser')
    PAGE += 1

with open('./workua.txt', 'w', encoding='utf-8') as outfile:
    for key, value in RESULT.items():
        outfile.write("link: {}, title: {}\n".format(key, value))

print("DONE")
