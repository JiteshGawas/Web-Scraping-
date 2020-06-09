import json
import time
from bs4 import BeautifulSoup
import requests
import time
import csv
import os

with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Timesjob.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Timesjob.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title','Company_Name','Location','Summary','Days_Posted_Ago','Experience','Skills'])

    url = "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords="+skill+"&txtLocation="+loc
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')
    #"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Science&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation="+mumbai+"&luceneResultSize=25&postWeek=60&txtKeywords="+skill+"&pDate=I&sequence=4&startPage=1
    for article in soup.find_all("li",{"class":"clearfix job-bx wht-shd-bx"}):

        exp = article.find("ul",{"class":"top-jd-dtl clearfix"}).li.text.strip()
        exp = exp.replace('card_travel','')
        exp = exp.replace('-','')
        exp = exp.replace('yrs',' ')
        #print(exp)
        #print(exp[0]+exp[1])
        #print(exp[3]+exp[4]+exp[5])
        if(expr > (exp[0]+exp[1]) and expr < (exp[3]+exp[4]+exp[5])):

        #print(article.prettify())
        

            title = article.h2.a.text.strip() 
            print(title)

            company = article.h3.text.strip()
            print(company.replace('(More Jobs)',''))

            location = article.find("ul",{"class":"top-jd-dtl clearfix"}).span.text.strip()
            print(location)

            summary = article.find("ul",{"class":"list-job-dtl clearfix"}).li.text.strip()
            print(summary)

            date = article.find("span",{"class":"sim-posted"}).text.strip()
            print(date)

            exp = article.find("ul",{"class":"top-jd-dtl clearfix"}).li.text.strip()
            print(exp.replace('card_travel',''))

            skills = article.find("span",{"class":"srp-skills"}).text.strip()
            print(skills)


            csv_print.writerow([title,company,location,summary,date,exp,skills])



            print("_______________________________________________________________________________________________________________________")
            time.sleep(2)