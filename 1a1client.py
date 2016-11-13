import requests, json

URL = "https://cloudpanel-api.1and1.com/v1"
headers={"X-TOKEN":"b148a362cb832e3fb58b114a1252024d"}

#get the names of your servers 
def getServerNames():
    this_url = URL + "/servers"
    r = requests.get(this_url, headers = headers)
    servers  = r.json()
    server_names = [server['name'] for server in servers]
    return server_names
    
#get the names of your servers 
def getServerIDs():
    this_url = URL + "/servers"
    r = requests.get(this_url, headers = headers)
    servers  = r.json()
    server_names = [server['name'] for server in servers]
    server_names = [server['name'] for server in servers]
    