#exp direct
#skills direct

from bs4 import BeautifulSoup
import requests
import time
import csv
import os


with open('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Shine.csv','a',encoding='utf-8',newline='') as f_output:
    csv_print = csv.writer(f_output)

    file_is_empty = os.stat('C:/Users/HP/Desktop/Internship-HR/Web-Scraping/Output/Job_Shine.csv').st_size == 0
    if file_is_empty:
        csv_print.writerow(['Job_Title','Company_Name','Location','Summary','Days_Posted_Ago','Experience','Skills'])
    pages = [2,3]


    for page in pages:
    #https://www.shine.com/job-search/data-science-jobs-in-mumbai


    #print(soup)
        source = requests.get("https://www.shine.com/job-search/"+skill+"-jobs-in-"+loc+"-{}".format(page)).text
        soup = BeautifulSoup(source,'lxml')

        for article in soup.find_all('li',class_='search_listing'):

        #print(article)
            exp = article.find('span',class_='snp_yoe cls_jobexperience').text.strip()
            exp = exp.replace('to','')
            #print(exp)
            #print(exp[0]+exp[1])
            #print(exp[3]+exp[4])
            if(expr > (exp[0]+exp[1]) and expr < (exp[3]+exp[4]+exp[5])):

                

                title = article.h3.text.strip()
                print(title)

                company = article.find('li',class_='snp_cnm cls_cmpname cls_jobcompany').text.strip()
                print(company)

                    
                location = article.find('em',class_='snp_loc').text.strip()
                print(location)
                    

                summary = article.find('li',class_='srcresult').text.strip()
                print(summary)

                
                date = article.find('li',class_='time share_links jobDate').text.strip()
                print(date)

                exp = article.find('span',class_='snp_yoe cls_jobexperience').text.strip()
                print(exp)

                skills = article.find("div",{"class":"sk jsrp cls_jobskill"}).text.strip()
                print(skills.replace("     ",""))

                csv_print.writerow([title,company,location,summary,date,exp,skills])

                print("--------------------------------")
                time.sleep(2)