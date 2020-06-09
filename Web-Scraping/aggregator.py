from bs4 import BeautifulSoup
import requests
import time
import csv
import os

skill = input("Enter the skills you want to search for : ")
loc = input("Enter the location you want to scrape : ").lower()


pages = [2,3]
for page in pages:
#https://www.shine.com/job-search/data-science-jobs-in-mumbai


#print(soup)
    source = requests.get("https://www.shine.com/job-search/"+skill+"-jobs-in-"+loc+"-{}".format(page)).text
    soup = BeautifulSoup(source,'lxml')

    for article in soup.find_all('li',class_='search_listing'):

    #print(article)

        title = article.h3.text.strip()
        print(title)

        date = article.find('li',class_='time share_links jobDate').text.strip()
        print(date)

        company = article.find('li',class_='snp_cnm cls_cmpname cls_jobcompany').text.strip()
        print(company)

            
        location = article.find('em',class_='snp_loc').text.strip()
        print(location)
            

        experience = article.find('li',class_='srcresult').text.strip()
        print(experience)

        print("--------------------------------")
        time.sleep(2)

print("__________________________________________________________Shine Over____________________________________________________________")

pages = [10,20,30,40]
with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Details.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Details.csv').st_size == 0
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

print("___________________________________________________________INDEED OVER__________________________________________________________________________________")


pages = [50,100,150,200]
for page in pages:
    my_url = 'https://www.freshersworld.com/jobs/jobsearch/'+skill+'-jobs-in-'+loc+'?&limit=50&offset={}'.format(page)
    source = requests.get(my_url).text
    soup = BeautifulSoup(source,'lxml')

    #print(soup.prettify())

    for article in soup.find_all("div", {"class": "col-md-12 col-lg-12 col-xs-12 padding-none job-container jobs-on-hover top_space"}):

        #print(article.prettify())

        #title
        company = article.a.h3.text.strip()
        print(company)

        title = article.find("div",{"class":"col-md-12 col-xs-12 col-lg-12 padding-none left_move_up"}).div.text
        print(title)

        education = article.find("span",{"class":"qualifications display-block modal-open"}).text
        print(education)

        location = article.find("span",{"class":"job-location display-block modal-open"}).text
        print(location)

        date = article.find("span",{"class":"ago-text"}).text
        print(date)

        print("_____________________________________________________________________________")
        time.sleep(2)

print("_________________________________________FRESHER'S WORLD OVER ___________________________________________________________________________")

pages = [1,2,3,4]

for page in pages:
    url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Science&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation="+loc+"&luceneResultSize=25&postWeek=60&txtKeywords="+skill+"&pDate=I&sequence={}".format(page)+"&startPage=1"
    source = requests.get(url).text
    soup = BeautifulSoup(source,'lxml')


    #"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Data%20Science&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation="+mumbai+"&luceneResultSize=25&postWeek=60&txtKeywords="+skill+"&pDate=I&sequence={}".format(page)"&startPage=1"
    for article in soup.find_all("li",{"class":"clearfix job-bx wht-shd-bx"}):

        #print(article.prettify())

        title = article.h2.a.text.strip()
        print(title)

        company = article.h3.text.strip()
        print(company)

        location = article.find("ul",{"class":"top-jd-dtl clearfix"}).span.text.strip()
        print(location)

        summary = article.find("ul",{"class":"list-job-dtl clearfix"}).li.text.strip()
        print(summary)

        date = article.find("span",{"class":"sim-posted"}).text.strip()
        print(date)

        print("_______________________________________________________________________________________________________________________")
        time.sleep(2)