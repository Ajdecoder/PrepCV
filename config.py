# from pymongo import MongoClient
# # MongoDB credentials
# MONGO_REMOTE_IP = "42.193.127.97"
# MONGO_REMOTE_PORT = 27042
# MONGO_AUTH_DB = "admin"
# MONGO_USER = "resumes.ai"
# MONGO_PASSWD = "resumsd"
# MONGOCLIENT = MongoClient(host=MONGO_REMOTE_IP, port=MONGO_REMOTE_PORT, username=MONGO_USER, password=MONGO_PASSWD,authSource=MONGO_AUTH_DB)
# # MONGOCLIENT = MongoClient(host=MONGO_REMOTE_IP, port=MONGO_REMOTE_PORT)
# DB_INSTANCE = MONGOCLIENT["prepcv"]



from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
uri = "mongodb+srv://omprakash:Omprakash@cluster0.l4cujqt.mongodb.net/?appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
DB_INSTANCE = client['prepcv']
