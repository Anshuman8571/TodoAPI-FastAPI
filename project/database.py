import os 
from dotenv import load_dotenv
from sqlalchemy import create_engine ,MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote

# What is an SQALchemy engine?
# An engine is factory of connection objects. 
# It-encapsulates-a-connection-pool-that-minimizes-the-cost-of-connecting-to-the-databse-by-reusing-existing-connections-and-provides-a-consistent-API-forworking with transaction
load_dotenv() # Load environment variable from the .env file 

DATABASE_URL = os.getenv("DATABASE_URL") 
# Get the DATABASE_URL-environment variable

engine = create_engine("mysql+pymysql://root:anshU114119118@localhost:3306/db", pool_size = 10,max_overflow=20) #create a SQALchemy engine

metadata_obj = MetaData()

Sessionlocal = sessionmaker(autocommit = False,autoflush=False,bind = engine) # create a SQALchemy session maker
Base = declarative_base() #Create a SQALchemy declarative base
