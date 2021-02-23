from logging import NullHandler
from os import link, write
import re
import string
from sys import excepthook
from urllib.parse import quote
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

def web(link, year, mth, day, RaceNo, loc, syr):
    driver = webdriver.Chrome('chromedriver')
    driver.get(link)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    tempwebstr = soup.find_all("div", {"id": "errorContainer"}) or None
        #print(str(soup.find_all("div", {"id": "errorContainer"})))
    if tempwebstr is not None:
        pass
    else:
        content = []
        RaceYr = year
        RaceMth = mth
        RaceDay = day
        RaceNum = RaceNo
        RaceLoc = loc
        temp = soup.find("td", {"colspan" : "16"}).getText().strip()
        temp1 = temp.split("(")
        temp2 = temp1[1].split(")")
        year1 = int(syr) + 1
        RaceID = syr + "/" + str(year1) + "-" + temp2[0] #identifer of Race (season + raceid)
        print("RaceID: " + RaceID)
        temp = ""
        temp = soup.find('td', {'style':'width: 385px;'}).getText()
        RaceClass = str(temp).split(" - ")[0]
        print("Class " + RaceClass)
        RaceLenth = str(temp).split(" - ")[1]
        print("Length " + RaceLenth)
        RaceGoing = soup.find('td', {'colspan': '14'}).getText()
        print("Going " + RaceGoing)
        RaceTrack = soup.find_all('td', {'colspan': '14'})
        print("Track: " + str(RaceTrack[1].getText()))
        TotalRaceTime = soup.find_all('td', {'style' : 'width:65px;'})
        i=0
        raceTime = []
        while i < (len(TotalRaceTime)):
            temp = ""
            temp1 = ""
            temp = TotalRaceTime[i].getText().split("(")
            temp1 = temp[1].split(")")
            raceTime.append(temp1[0])
            temp = ""
            temp1 = ""
            i = i + 1
        print(raceTime)
            

    driver.close()

def main():
    #Fetch all race data from 2009/10 - 2019/20
    syr = "19"
    year = "20" + syr
    mth = "09"
    day = "01"
    num = "1"
    loc = "ST"
    #loc = "HV" 
    link = 'https://racing.hkjc.com/racing/information/English/Racing/LocalResults.aspx?RaceDate=' + year + '/' + mth + '/'+ day + "&Racecourse=" + loc + "&RaceNo=" + num
    web(link=link, year=year, mth=mth, day=day, RaceNo=num, loc=loc, syr=syr)



if __name__ == '__main__':
    main()