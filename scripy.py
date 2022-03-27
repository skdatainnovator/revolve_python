#importing necessaries libraries
import tarfile
import pandas as pd
import datetime

file = tarfile.open('data.tar.gz')

file.extractall('./data')
file.close()

#Loading all the dataframe

flights = pd.read_csv("./data/data/flights.csv")
airlines = pd.read_csv("./data/data/airlines.csv")
airports = pd.read_csv("./data/data/airports.csv")
planes = pd.read_csv("./data/data/planes.csv")
weather = pd.read_csv("./data/data/weather.csv")


def no_of_days_FlightsCover(flights):
    first_day = flights.iloc[0,2]
    first_month = flights.iloc[0,1]

    last_day = flights.iloc[-1,2]
    last_month = flights.iloc[-1,1]


    time1 = datetime.date(2013,first_month,first_day)
    time2 = datetime.date(2013,last_month,last_day)

    return (time2-time1).days

no_of_days_FlightsCover(flights) 
## 272 days


def no_of_dep_cities(flights,airports):
    dep_city = flights['origin'].unique()
    uni_city = []
    for i in range(len(dep_city)):
        df = airports[airports['IATA_CODE']==dep_city[i]]
        city = df.iloc[0,1]
        uni_city.append(city)
    
    return uni_city

no_of_dep_cities(flights=flights,airports=airports)
# ['Newark Liberty International Airport',
#  'LaGuardia Airport (Marine Air Terminal)',
#  'John F. Kennedy International Airport\xa0(New York International Airport)']


def rel_bw_flights_planes():
    
    return 'The Planes Tables are the detailes information of the planes that flights table have.'
rel_bw_flights_planes()
# The Planes Tables are the detailes information of the planes that flights table have.


def most_delays_manufacture(flights,planes):
    con_df = flights.merge(planes,on='tailnum',how='right')
    df4 = con_df.groupby('manufacturer')['dep_delay'].sum().sort_values(ascending=False).head(1)

    return df4.index[0]

most_delays_manufacture(flights,planes)
# 'EMBRAER'



def most_connected_cities(flights):
    cities = flights.groupby(['origin','dest']).size().sort_values().tail(1).index[0]
    uni_city = []
    for i in range(len(cities)):
        df = airports[airports['IATA_CODE']==cities[i]]
        city = df.iloc[0,1]
        uni_city.append(city)
    
    return uni_city[0] , uni_city[1]

most_connected_cities(flights)
# ('John F. Kennedy International Airport\xa0(New York International Airport)',
#  'Los Angeles International Airport')
 