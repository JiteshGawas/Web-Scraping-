from bs4 import BeautifulSoup
import requests
import time
import csv
import os

pages = [10,20,30,40]
with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Indeed.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Indeed.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title','Company_Name','Location','Summary','Days_Posted_Ago'])


    for page in pages:
        source = requests.get("https://www.indeed.co.in/jobs?q="+skill+"&l="+loc+"&start={}".format(page)).text

        soup = BeautifulSoup(source,'lxml')

        #print(soup.prettify())

        for article in soup.find_all('div',class_='jobsearch-SerpJobCard'):
            #print(article) 


            try:
                title = article.h2.a.text.strip()   # Title of the job
            except Exception as e:
                title = None
            print(title)


            try:
                name = article.find('span',class_='company').text.strip()  # company name
            except Exception as e:
                name = None
            print(name)


            try:
                location = article.find(class_='location accessible-contrast-color-location').text.strip()    # location of job 
            except Exception as e:
                location = None
            print(location)


            try:
                summary = article.find('div',class_='summary').text.strip()        # summary of job
            except Exception as e:
                summary = None
            print(summary)


            try:
                date = article.find('span',class_='date').text.strip()       #date posted
            except Exception as e:
                date = None
            print(date)


            csv_print.writerow([title,name,location,summary,date])


            print("---------------------------------------------------")
            

            time.sleep(2)