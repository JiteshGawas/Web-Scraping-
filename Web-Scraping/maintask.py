from bs4 import BeautifulSoup
import requests
import time
import csv
import os

url = input("Enter the url you want to scrape : ")
#skillset
#loc

loc = input("Enter the location you want to scrape : ")

with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Combined.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Combined.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title','Company_Name','Location','Summary','Days_Posted_Ago'])


    s=url.split(sep='.')
    if 'shine' in s:
                                
        pages=[2,3,4,5]
        for page in pages:

            source = requests.get(url+"-{}".format(page)).text
            soup = BeautifulSoup(source,'lxml')

            for article in soup.find_all('li',class_='search_listing'):
            #print(article)
                l1=article.find('em',class_='snp_loc').text.strip()
                if loc in l1:

                    try:
                        title = article.h3.text.strip()
                    except Exception as e:
                        title = None
                    print(title)

                    try:
                        company = article.find('li',class_='snp_cnm cls_cmpname cls_jobcompany').text.strip()
                    except Exception as e:
                        company = None
                    print(company)

                    try:
                        location = article.find('em',class_='snp_loc').text.strip()
                    except Exception as e:
                        location = None
                    print(location)

                    try:
                        summary = article.find('li',class_='srcresult').text.strip()
                    except Exception as e:
                        summary = None
                    print(summary)

                    try:
                        date = article.find('li',class_='time share_links jobDate').text.strip()
                    except Exception as e:
                        date = None
                    print(date)

                    csv_print.writerow([title,company,location,summary,date])

                    print("------------------------------")
                    time.sleep(2)
                else:
                    break

    elif 'indeed' in s:

        pages = [10,20,30]

        for page in pages:
            source = requests.get(url+"&start={}".format(page)).text
            soup = BeautifulSoup(source,'lxml')
            
            for article in soup.find_all('div',class_='jobsearch-SerpJobCard'):

                l1 = article.find(class_='location accessible-contrast-color-location').text.strip()
                 
                if loc in l1:

                    try:
                        title = article.h2.a.text.strip()   # Title of the job
                    except Exception as e:
                        title = None
                    print(title)


                    try:
                        company = article.find('span',class_='company').text.strip()  # company name
                    except Exception as e:
                        company = None
                    print(company)


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

                    csv_print.writerow([title,company,location,summary,date])

                    print("--------------------------------------")
                    
                    time.sleep(2)
                else:
                    break

    else:
        print("Not found page")
                