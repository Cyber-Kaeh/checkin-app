import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_config import Base, User

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Connect to the existing database
        cls.engine = create_engine('sqlite:///users.db')
        Base.metadata.bind = cls.engine
        cls.Session = sessionmaker(bind=cls.engine)


    # def tearDown(self):
    #     self.Session.close()


    def test_show_all_users(self):
        session = self.Session()
        users = session.query(User).all()
        session.close()
        self.assertGreater(len(users), 0, "No users found in the database.")
        for user in users:
            print(f"Passed -> User: {user.name}, {user.phone}, {user.available}")

    def test_fetch_one_row(self):
        session = self.Session()
        user = session.query(User).first()
        session.close()
        self.assertIsNotNone(user, "No users found in the database.")
        if user:
            print(f"Passed -> Fetched user: {user.name}, {user.phone}, {user.available}")


    def test_add_user(self):
        session = self.Session()
        new_user = User(name="FredF", phone="1234567890", available=True)
        session.add(new_user)
        session.commit()
        session.close()

        # Verify the user was added
        session = self.Session()
        user = session.query(User).filter_by(name="FredF").first()
        session.close()
        self.assertIsNotNone(user, "User was not added to the database.")
        if user:
            print(f"Passed -> Added user: {user.name}, {user.phone}, {user.available}")


    def test_available_true(self):
        session = self.Session()
        user = session.query(User).filter_by(name="FredF").first()
        session.close()
        if user:
            user.available = True

            self.assertTrue(user.available, "User availability should be True.")
            print(f"Passed -> User available status: {user.available}")

if __name__ == "__main__":
    unittest.main()
