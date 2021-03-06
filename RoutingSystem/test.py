
import numpy as np
from geopy.geocoders import Nominatim
import  regex as re

#Finding the latitude and longitude and storing them in separate lists
geolocator = Nominatim(user_agent="my_user_agent")
CityCenterListData=['Electronic City,Bangalore',
                    'BTM Layout,Bangalore',
                    'Rajajinagar, Bengaluru, Karnataka',
                    'Brookefield, Bengaluru, Karnataka',
                    'Kengeri, Bengaluru, Karnataka 560060',
                    'Kumaraswamy Layout, Bengaluru, Karnataka 560078',
                    'Bellandur, Bengaluru, Karnataka'
                    ]
LatitudeList=[]
LongitudeList=[]
i=0
for address in CityCenterListData:
        loc = geolocator.geocode(address)
        LatitudeList.append(loc.latitude)
        LongitudeList.append(loc.longitude)

# from [https://ipython-books.github.io/147-creating-a-route-planner-for-a-road-network/]

# from [https://stackoverflow.com/a/8859667/1595060](https://stackoverflow.com/a/8859667/1595060)

#Finding the distance between two places using there latitudes and ongitudes
EARTH_R = 6372.8

def geocalc(lat0, lon0, lat1, lon1):
    """Return the distance (in km) between two points
    in geographical coordinates."""
    lat0 = np.radians(lat0)
    lon0 = np.radians(lon0)
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    dlon = lon0 - lon1
    y = np.sqrt((np.cos(lat1) * np.sin(dlon)) ** 2 +
        (np.cos(lat0) * np.sin(lat1) - np.sin(lat0) *
         np.cos(lat1) * np.cos(dlon)) ** 2)
    x = np.sin(lat0) * np.sin(lat1) + \
        np.cos(lat0) * np.cos(lat1) * np.cos(dlon)
    c = np.arctan2(y, x)
    return EARTH_R * c


#Function to find the nearest city from the given city
def find_nearest(lat,long):
    MinValue=999999999
    MinValuePlace=""
    for i in range(0,len(CityCenterListData)):
        TempValue=geocalc(lat, long, LatitudeList[i], LongitudeList[i])
        if TempValue<MinValue:
            MinValue=TempValue
            MinValuePlace=CityCenterListData[i]
        # print(CityCenterListData[i] + " is " + str(TempValue) + "\n")

    return MinValuePlace


# Input the Place for which we want to calculate the nearest station
place=input("Input the Place for which we want to calculate the nearest station\n").lower()

lat=0
long=0
loc = geolocator.geocode(place)
lat=loc.latitude
long=loc.longitude
MinValue = 999999999
MinValuePlace = ""
for i1 in range(0, len(CityCenterListData)):
    TempValue = geocalc(lat, long, LatitudeList[i1], LongitudeList[i1])
    if TempValue < MinValue:
        MinValue = TempValue
        MinValuePlace = CityCenterListData[i1]
    # print(CityCenterListData[i] + " is " + str(TempValue) + "\n")
print("Nearest to " + place +" is " + MinValuePlace)


