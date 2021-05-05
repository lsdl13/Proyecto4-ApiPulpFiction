import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()

dburl=os.getenv("URL")

print(dburl)
if not dburl: 
    raise ValueError("no tienes url mongodb")

#Vamos a conectar con la base de datos 
client = MongoClient("localhost:27017")
db = client.get_database("PulpFiction")
collection=db["pfscript"]


