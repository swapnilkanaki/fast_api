from pymongo import MongoClient
import pymongo
import dns.resolver

dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

conn_str = "mongodb+srv://temptest:temptest@cluster0.d9iwduc.mongodb.net/?retryWrites=true&w=majority"
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)
collecton_name =None
try:
    print(client.server_info())
    db = client.testingDB
    collecton_name = db['dataUse']
except Exception:
    print("Unable to connect to the server.")


# client = pymongo.MongoClient("mongodb+srv://temptest:temptest@cluster0.d9iwduc.mongodb.net/?retryWrites=true&w=majority")
# # db = client.test
# db = client.testingDB


# # testingDB.dataUse
# collecton_name = db['dataUse']