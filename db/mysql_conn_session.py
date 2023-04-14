from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin:123456@localhost:3306/battery_data", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
