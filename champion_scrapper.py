from constants import Elo, Role
from util import tierlist_formatter
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def get_champions(role: Role, elo: Elo):
    url = tierlist_formatter(role, elo)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)  # Add a short sleep to allow the content to load after scrolling

    to_puto = driver.find_elements(By.XPATH, ".//div[@class='rt-tr-group']")

    champions = []
    regex_pattern = re.compile(r'\/lol\/champions\/(\w+).*')

    for element in to_puto:
        a_tag = element.find_element(By.XPATH, ".//a")
        if not a_tag: continue
        href = a_tag.get_attribute('href')
        match = regex_pattern.search(href)
        if match:
            champion_name = match.group(1)
            champions.append(champion_name)
        else:
            print(href)

    driver.quit()
    unique_champions = list(set(champions))
    unique_champions.sort()
    return unique_champions, len(unique_champions) 

# Example usage
role = Role.ADC
elo = Elo.PLATINUM
champion_names = get_champions(role, elo)
print(champion_names)