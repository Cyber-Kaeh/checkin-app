from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash, check_password_hash

engine = create_engine('sqlite:///users.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    available = Column(Boolean, default=False, nullable=False)

    def set_phone(self, phone):
        self.phone_hash = generate_password_hash(phone)

    def check_phone(self, phone):
        return check_password_hash(self.phone_hash, phone)


def add_sample_data():
    sess = Session()
    user1 = User(name="JohnD", phone="7045551111", available=True)
    user1.set_phone("7045551111")
    user2 = User(name="BobB", phone="7045552222", available=False)
    user2.set_phone("7045552222")
    sess.add_all([user1, user2])
    sess.commit()
    sess.close()


def drop_db():
    Base.metadata.drop_all(engine)


def init_db():
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    drop_db()
    init_db()
    add_sample_data()
    print("Databaes intialized. Name: users.")
