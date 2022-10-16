from ApiFunctions import *
import pandas as pd
from geopy import *

practioners = getRequest('Practitioner')

practionerContacts = []
for practioner in practioners:
    
    zipcode = practioner['resource']['address'][0]['postalCode']
    if len(zipcode) > 5:
        zipcode = zipcode[0:5]
    elif len(zipcode) < 5:
        while len(zipcode) < 5:
            zipcode = '0' + zipcode
    
    email = practioner['resource']['telecom'][0]['value']
    
    location = practioner['resource']['address'][0]
    locationLine = f"{location['line'][0]}, {location['city']}, {location['state']} {zipcode}"

    locator = Nominatim(user_agent='myGeocoder')
    loc = locator.geocode('locationLine')
    
    practionerContacts.append([locationLine, loc.latitude, loc.longitude, email])
    #print([locationLine, loc.latitude, loc.longitude, email])

df = pd.DataFrame(practionerContacts, columns=['Address', 'Longitude', 'Latitude' 'Email'])
df.to_csv('PractionerContacts', index=False)