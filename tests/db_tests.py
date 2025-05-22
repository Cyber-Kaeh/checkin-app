import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db_config import Base, User

class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine('sqlite:///users.db')
        Base.metadata.bind = cls.engine
        cls.Session = sessionmaker(bind=cls.engine)

    def setUp(self):
        # Start a new connection and transaction for each test
        self.connection = self.engine.connect()
        self.trans = self.connection.begin()
        self.session = self.Session(bind=self.connection)

    def tearDown(self):
        # Rollback the transaction and close the connection
        self.session.close()
        self.trans.rollback()
        self.connection.close()

    def test_show_all_users(self):
        users = self.session.query(User).all()
        self.assertGreater(len(users), 0, "No users found in the database.")
        for user in users:
            print(f"All Users: -> User: {user.name}, {user.phone}, {user.available}")

    def test_fetch_one_row(self):
        user = self.session.query(User).first()
        self.assertIsNotNone(user, "No users found in the database.")
        if user:
            print(f"Passed -> Fetched user: {user.name}, {user.phone}, {user.available}")

    def test_add_user(self):
        new_user = User(name="FredF", phone="1234567890", available=True)
        self.session.add(new_user)
        self.session.commit()
        user = self.session.query(User).filter_by(name="FredF").first()
        self.assertIsNotNone(user, "User was not added to the database.")
        if user:
            print(f"Passed -> Added user: {user.name}, {user.phone}, {user.available}")

    def test_available_true(self):
        user = self.session.query(User).filter_by(name="FredF").first()
        if user:
            user.available = True
            self.session.commit()
            self.session.refresh(user)
            self.assertTrue(user.available, "User availability should be True.")
            print(f"Passed -> User available status: {user.available}")

if __name__ == "__main__":
    unittest.main()