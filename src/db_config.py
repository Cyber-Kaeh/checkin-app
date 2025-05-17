from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    available = Column(Boolean, default=False, nullable=False)


def add_sample_data():
    sess = Session()
    user1 = User(name="JohnD", phone="7045551111", available=True)
    user2 = User(name="BobB", phone="7045552222", available=False)


def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    init_db()
    add_sample_data()
    print("Databaes intialized. Name: users.")
