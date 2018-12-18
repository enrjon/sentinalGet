import os
import requests

# directories
workingDir = "SentinelGet"
rawDir = "raw"
tiffDir = "tiff"

os.chdir(workingDir)

# credentials
creds = open("foobar.config")
username = "testUser"
password = "testPass"

# url base
baseURL = "https://scihub.copernicus.eu/dhus/search?"


#### QUERY PARAMETERS ####

# How far back to search; last 10 days
dateFilter = "beginposition:[NOW-10DAYS TO NOW] AND endposition:[NOW-10DAYS TO NOW]"

# result management
paginationStart = 0 # pagination result position
paginationRows = 20 # results per page(100 maximum)

# product name (sentinel-2 data)
platformFilter = "platformname:Sentinel-2"

#print(baseURL)
#print(timeCriteria)
#print("working directory is " + os.getcwd())