#Import libraries.
import json 
from urllib.request import urlopen

 
#Query the API for the particular data.
def start():
    countries_url = r'https://api.dhsprogram.com/rest/dhs/countries'
    country_name = input("Enter Name of Country to search for > ") 
    
    

    request = urlopen(countries_url)
    response = json.loads(request.read())
    answer = response['Data']
   

    if country_name == 'Zambia':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/ZM'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

            print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()

    elif country_name == 'Angola':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/AO'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

            print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()

    elif country_name == 'Zimbabwe':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/ZW'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

            print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()

    elif country_name == 'Angola':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/AO'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

   e        print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()

    elif country_name == 'Tanzania':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/TZ'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

            print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()

    elif country_name == 'Namibia':

        def start():
            data_url = r'https://api.dhsprogram.com/rest/dhs/surveys/NM'
   

             #Obtain and Parse the list into a Python Object.
            req = urlopen(data_url)
            resp = json.loads(req.read())
            my_data = resp['Data']
 
            #Display a list of each characteristic and their value.

            print('Survey released Date: {}'.format(my_data[0]['ReleaseDate']))
            print('Survey ID: {}'.format(my_data[0]['SurveyId']))
            print('Survey Type: {}'.format(my_data[0]['SurveyType']))
            print('Survey Country: {}'.format(my_data[0]['CountryName']))
            print('Survey number: {}'.format(my_data[0]['SurveyNum']))
            print('This survey started on: {}'.format(my_data[0]['FieldworkStart']))
            print('Number of Recoreded Women: {}'.format(my_data[0]['NumberOfWomen']))
            print('Implementing Organisation: {}'.format(my_data[0]['ImplementingOrg']))
            print('Indicator Data: {}'.format(my_data[0]['IndicatorData']))   
            print('Max Number of Men: {}'.format(my_data[0]['MaxAgeMen']))
            print('Survey Number: {}'.format(my_data[0]['SurveyNum']))
        start()


    else:
        print("Kindly search for Zambia, Angola, Zimbabwe, Namibia, Tanzania")

start()

input('press ENTER to exit')  
