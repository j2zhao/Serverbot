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
    
#get the ids of your servers 
def getServerIDs():
    this_url = URL + "/servers"
    r = requests.get(this_url, headers = headers)
    servers  = r.json()
    server_names = [server['name'] for server in servers]
    server_ids = [server['name'] for server in servers]
    server_dic = {}
    for i in range(len(server_names)):
        server_dic[server_names[i]] = server_ids[i]
    return server_dic
    
#get status of a server
def getServerStatus(id):
    this_url = URL + "/servers/" + id + "/status"
    r = requests.get(this_url, headers = headers)
    status  = r.json()
    return status

#get hdd sizes of a server
def getServerHDD(id):
    this_url = URL + "/servers/" + id + "/hardware/hdds"
    r = requests.get(this_url, headers = headers)
    hdds  = r.json()
    server_hdds = [server['size'] for server in servers]
    return  server_hdds

#clone server
# "name": "Copy of My server",
# "datacenter_id": "D0F6D8C8ED29D3036F94C27BBB7BAD36"
#return 200 is successful
def cloneServer(id, name, datacenter_id):
    this_url = URL + "/servers/" + id + "/clone"
    data = {"name": name, "datacenter_id": datacenter_id}
    req = requests.post(this_url, data = data, headers = headers);
    return req.status_code

#set hdd sizes of a server
#"size": 40,
#"is_main": false
#return 202 is successful
def getServerHDD(id, size, main):
    data = {"hdds": [{"size": size, "is_main": false}]}
    this_url = URL + "/servers/" + id + "/hardware/hdds"
    req = requests.post(this_url, data = data, headers = headers);
    return req.status_code
    
    
    
    