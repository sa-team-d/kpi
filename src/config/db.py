import os
from model.model import Base
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

database_url = os.getenv("DATABASE_URL")
debug_mode = os.getenv("DEBUG")

engine = create_engine(database_url)
Base.metadata.create_all(engine)

def createSession():
    Session = sessionmaker(bind=engine)
    return Session()


# Function to refresh a detached instance
def refreshData(data_instance):
    Session = sessionmaker(bind=engine)
    with Session() as new_session:  # Create a new session
        new_session.refresh(data_instance)  # Refresh from the database
        return data_instance