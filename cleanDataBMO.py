from bs4 import BeautifulSoup
import os

directory = './transcripts/'

# write/open file
compiled_scripts = open("scripts.html", "w")

# helper function
def clean_data(soup):
    scripts = soup.find_all('dl')
    for line in scripts:
        compiled_scripts.write(str(line) + "\n")

# iterate through folder and assign each file to html_doc,
# then find the script lines(if 'dl' tag exists) and call clean_data
for file in os.listdir(directory):
    html_doc = open(directory + file, 'r')
    soup = BeautifulSoup(html_doc, 'html.parser')
    if soup.find('dl') is not None:
        clean_data(soup)
    else:
        continue

# close file
compiled_scripts.close()