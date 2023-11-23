from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, sessionmaker, declarative_base
from flask_login import UserMixin

Base = declarative_base()

class User(Base, UserMixin):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    balance = Column(Integer, nullable=False, default=0)



engine = create_engine('sqlite:///app.db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)


session = Session()