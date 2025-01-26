import os
from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

# create connection
database_url = "mysql+pymysql://{user}:{pwd}@{host}:{port}/{db}"

engine = create_engine(database_url.format(
    user=os.getenv("DB_USER"), pwd=os.getenv("PASSWORD"), host=os.getenv("HOST"), port=os.getenv("PORT"), db=os.getenv("DATABASE")
), echo=True)

# setup tables
Base.metadata.create_all(bind=engine)

# make a session class for same db
Session = sessionmaker(bind=engine)