import os
import requests
import configparser
import HTTPDigestAuth

# directories
workingDir = "sentinelGet"
rawDir = "raw"
tiffDir = "tiff"

os.chdir(workingDir)

# credentials
config = configparser.ConfigParser()
config.read("foobar.ini")
username = config['USER PASSWORD']['username']
password = config['USER PASSWORD']['password']

# url base
baseURL = "https://scihub.copernicus.eu/dhus/search?"

#inital request to verify credentials
from requests.auth import HTTPBasicAuth
requests.get(baseURL, auth = HTTPBasicAuth(username, password))

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