import os
import urllib2

# credentials
username = "testUser"
password = "testPass"

# url base
baseURL = "https://scihub.copernicus.eu/dhus/search?"


# directories
os.chdir("D:\Program "

# How far back to search; last 10 days
timeCriteria = "beginposition:[NOW-10DAYS TO NOW] AND endposition:[NOW-10DAYS TO NOW]"

print(baseURL)
print(timeCriteria)
print("working directory is " + os.getcwd())