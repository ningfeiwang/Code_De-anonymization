#!/usr/local/bin/python
# coding:utf-8
# import urllib
from urllib import urlopen
from urllib import urlretrieve
import urllib
import requests
from selenium import webdriver
import BeautifulSoup as BS
import json
import sys
import os
import zipfile
import shutil
import multiprocessing
import time
# import phantomjs

# returns the URL to download the user submission
# https://code.google.com/codejam/contest/32011/dashboard#s=p3
def get_download_url(competition_id, num):
    if num == 0:
         return "http://code.google.com/codejam/contest/" \
                + competition_id \
                + "/dashboard" 
    else:
        return "http://code.google.com/codejam/contest/" \
                    + competition_id \
                    + "/dashboard#s=p" \
                    + str(num)
def getHtml(url):
    page = urlopen(url)
    html = page.read()
    return html

def writefile(filename, content):
    with open(filename,'w') as f:
        f.write(content)


def craw(year, competition_id, problems):
    for i in range(0, len(problems)):

        url = get_download_url(competition_id, i)
        print url   
        driver = webdriver.Chrome()
        # driver.find_elements_by_xpath('//*[@id="dsb-problem-content-div0"]/div/table/tbody/tr[2]/td[1]/code')
        # print driver.page_source
        driver.get(url)
        time.sleep(4)
        path = '//*[@id="dsb-problem-content-div' + str(i) + '"]/div/table/tbody/tr[2]/td[1]/code'
        print path
        a = driver.find_elements_by_xpath(path)
        # driver.quit()
        # print a[0].text
        name = problems[i]["id"] + ".txt"
        writefile(name, a[0].text)

        driver.quit()
        # //*[@id="dsb-problem-content-div1"]/div/table/tbody/tr[2]/td[1]/code
        # if i == 1:
        #     break



# main section of script
if __name__ == '__main__':
    script_path = os.path.dirname(os.path.realpath(__file__))
    metadatafile = open(script_path + "/CodeJamMetadata.json").read()
    metadata = json.loads(metadatafile)

    # loop through years
    for year_json in metadata['competitions']:
        year = year_json['year']

        # loop through rounds
        for round_json in year_json['round']:
            round_id = round_json['contest']
            problems = round_json['problems']

        # print year
        # print round_id
        # print problems[1]["id"]
            craw(year, round_id, problems)
        # break

            # run scraper on current round
            # scraper = multiprocessing.Process(target=scrape, args=(round_id, problems, script_path))
            # scraper.start()
