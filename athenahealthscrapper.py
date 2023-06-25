# this code is used to scrap the athenahealth website for the list of the clinics
# and their details and store it in a csv file

import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#This function takes in the clinic id and returns the clinic name
def get_clinic_name(clinic_id):
    url = f"https://{clinic_id}.portal.athenahealth.com/"
    r = requests.get(url)
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    clinic_name = soup.find_all('h1')[-1].text.strip()
    #print(clinic_name)
    return clinic_name

#get_clinic_name(12696)
#this variables are used to set the range of the clinic ids
start= 12690
end = 12710

#this loop is used to iterate through the clinic ids and store the clinic id and clinic name in a dictionary
master_list = []
for clinic_id in range(start, end):
    data_dict = {}
    data_dict['clinic_id'] = clinic_id
    data_dict['clinic_name'] = get_clinic_name(clinic_id)
    if data_dict['clinic_name'] != "Payment Confirmation" and data_dict['clinic_name'] != "Sorry, we can't find that practice. Make sure you typed the right address.":
        master_list.append(data_dict)

#this code is used to store the dictionary in a csv file
df = pd.DataFrame(master_list)
df.to_csv('athenahealth.csv', index=False)
print(df)




