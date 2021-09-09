# Ensure installation of requests and beautifulsoup4 before running
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import os

# Set up project
url = 'https://adventuretime.fandom.com/wiki/Category_talk:Transcripts'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
os.mkdir("./transcripts")

# Filter for links to each transcript page using regex
def only_transcripts(href):
    return href and re.compile("/Transcript").search(href)

# Create list of links
transcriptList = soup.find_all(href=only_transcripts)

# For each link, assign tag href to 'link' and 
# tag title to 'title' while cleaning the title data to suit file naming. 
# After, save the file to the designated folder and pause the scraper to not overload servers.
for each_tag in transcriptList:
    link = each_tag['href']
    title = each_tag['title'][:-11].replace(" ", "")
    dload_url = "https://adventuretime.fandom.com" + link 
    urllib.request.urlretrieve(dload_url, './transcripts/' + title + '.html')
    time.sleep(1)