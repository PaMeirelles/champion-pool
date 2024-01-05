from constants import Elo, Role
from util import tierlist_formatter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time

def get_champions(role: Role, elo: Elo, debug=False):
    url = tierlist_formatter(role, elo)
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(10)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3) 

    rows = driver.find_elements(By.XPATH, ".//div[@class='rt-tr-group']")

    champions = []
    regex_pattern = re.compile(r'\/lol\/champions\/(\w+).*')

    for row in rows:
        a_tag = row.find_element(By.XPATH, ".//a")
        if not a_tag: continue
        href = a_tag.get_attribute('href')
        match = regex_pattern.search(href)
        if match:
            champion_name = match.group(1)
            champions.append(champion_name)
        else:
            if debug:
                print(f"Link {href} não passou no regex")
    driver.quit()
    unique_champions = list(set(champions))
    if debug:
        print(f"{len(unique_champions)} campeões diferentes")
    return unique_champions

# Example usage
role = Role.SUPPORT
elo = Elo.PLATINUM
champion_names = get_champions(role, elo, debug=True)
print(champion_names)