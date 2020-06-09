from bs4 import BeautifulSoup
import requests
import time
import csv
import os


with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Indeed.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Indeed.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title','Company_Name','Location','Summary','Days_Posted_Ago','Experience'])
        source = requests.get("https://www.indeed.co.in/jobs?q=data+science&l=Mumbai").text
        soup = BeautifulSoup(source,'lxml')

        for article in soup.find_all('div',class_='jobsearch-SerpJobCard'):
                #print(article) 



                title = article.h2.a.text.strip()   # Title of the job
                print(title)

                company = article.find('span',class_='company').text.strip()  # company name
                print(company)

                location = article.find(class_='location accessible-contrast-color-location').text.strip()    # location of job 
                print(location)

                summary = article.find('div',class_='summary').text.strip()        # summary of job
                print(summary)

                date = article.find('span',class_='date').text.strip()       #date posted
                print(date)

                l = article.h2.a.get('href')
                ind ="https://www.indeed.co.in"
                url1 = ind+l
                #print(url1)

                source1 = requests.get(url1).text
                soup = BeautifulSoup(source1,'lxml')
                #print(soup.prettify())

                exp = soup.find("div",{"class":"jobsearch-JobMetadataHeader icl-u-xs-mb--md"}).text
                print(exp)

                #print(exp)
                csv_print.writerow([title,company,location,summary,date,exp])


                print("---------------------------------------------------")
