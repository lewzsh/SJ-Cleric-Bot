from os import sep
from bs4 import BeautifulSoup
import re
import pandas as pd

data = {
    'name': [],
    'line': []
}

with open('scripts.html') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

action_regex = '[\(\[].*?[\)\]]'

for line in soup.find_all('dd'):
    if line.find('b') is not None:
        character = line.b.extract().get_text()
        character = re.sub(action_regex, "", character)
        rest = line.get_text()
        rest = re.sub(action_regex, "", rest)
        rest = rest.replace(":", "")
        if rest == " " or rest == "":
            continue
        else:
            data['name'].append(character)
            data['line'].append(rest)

df = pd.DataFrame(data)

df.to_csv('AT_scripts.csv', sep='|', index=False)