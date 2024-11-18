import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

database_url = os.getenv("DATABASE_URL")
debug_mode = os.getenv("DEBUG")

client = MongoClient(database_url)
db = client['smart_app']
machines_collection = db['machines']
kpis_collection = db['kpis']