
import pandas as pd
import requests
from bs4 import BeautifulSoup

path='https://www.mudah.my'

df1=pd.read_excel('WebScrapingData_prova.xlsx',index_col=0)

#array=['/Pembantu+am-88630910.htm','/Team+Leader+dan+Rigger-88626981.htm','/Mekanik-88621635.htm']
rows_list=[]
try:
  for p in df1["URL"].tolist():
    page= requests.get(path+p)

    #page= requests.get(' put here your link')

    soup= BeautifulSoup(page.content , 'html.parser')

    #JOB DETAILS
    job=soup.find(class_='mw13 mw151')
    job_description=job.get_text()
    table = soup.find('table', {'class':'mw161 mw154'}) 
    table1 = soup.find('table', {'class':'mw192 mw185'})
    if table or table1:
      
      td = table.find('td', text='Contract Type')
      td_1 = td.findNext()
      contractType=td_1.get_text()
      td = table.find('td', text='Job Type')
      td_1 = td.findNext()

      jobType=td_1.get_text()
      td = table.find('td', text='Experience Level')
      td_1 = td.findNext()
      expLev=td_1.get_text()
      td = table.find('td', text='Job Categories')
      td_1 = td.findNext()
      jobC=td_1.get_text()

      td = table.find('td', text='Minimum Education Required')
      td_1 = td.findNext()
      minEd=td_1.get_text()

      td = table.find('td', text='Language Required')
      td_1 = td.findNext()
      languages=td_1.get_text()

      td = table.find('td', text='Nationality Preferred')
      td_1 = td.findNext()
      nationality=td_1.get_text()

      td = table.find('td', text='Gender Preferred')
      td_1 = td.findNext()
      gender=td_1.get_text()

      td = table.find('td', text='Own Transport')
      td_1 = td.findNext()
      transport=td_1.get_text()

      #benefits??
      #Telephone Number
      #Company No
      #Email

      #here we use pandas
      details={}
      details.update({'Job description':job_description,'Contract Type':  contractType, 'Job Type':jobType, 'Experience Level':  expLev,
      'Job Categories':jobC,'Minimum Education Required': minEd,'Language Required':  languages,'Nationality Preferred':  nationality,'Gender Preferred':  gender,'Own Transport':  transport})
      rows_list.append(details)


  df1 = pd.DataFrame(rows_list) 
  df1.to_csv('output.csv')



except Exception as e: # work on python 3.x
  print("exception"+ str(e))

