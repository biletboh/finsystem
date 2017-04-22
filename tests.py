import unittest
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models


class RolesModelTestCase(unittest.TestCase):
    """Test Project models."""

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = scoped_session(sessionmaker(
                                                autocommit=False,
                                                autoflush=False,
                                                bind=self.engine))
        Base.query = self.session.query_property()
        Base.metadata.create_all(bind=self.engine)
        client1 = models.Client(
                            id=1, first_name='John',
                            last_name='Doe', email='johndoe@mail.com',
                            balance=0)
        self.session.add(client1)
        manager1 = models.Manager(
                                id=1, username='Helper')
        self.session.add(manager1)
        self.session.commit()

        
    def test_client_model(self):
        clients = self.session.query(models.Client).all()
        assert len(clients) == 1

    def test_manager_model(self):
        managers = self.session.query(models.Manager).all()
        assert len(managers) == 1

    def tearDown(self):
        self.session.remove()


class RegisterEndpointTestCase(unittest.TestCase):
    """Test register endpoint."""

    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.session = scoped_session(sessionmaker(
                                                autocommit=False,
                                                autoflush=False,
                                                bind=self.engine))
        Base.query = self.session.query_property()
        Base.metadata.create_all(bind=self.engine)
        self.client_info = {
                    id=1, first_name='John', last_name='Doe', 
                    email='johndoe@mail.com'}

    def register(
                self, first_name, last_name, email=None,
                password, password2=None,):
        """Use helper function to register a user."""
        
        if password2 is None:
            password2 = password
        if email is None:
            email = username + '@example.com'
        return self.post('/register', data={
                                            'first_name': first_name,
                                            'last_name': first_name,
                                            'email': email,
                                            'password': password,
                                            'password2': password2,
                                            }, follow_redirects=True)

        
    def test_register_endpoint(self):
       """Make sure registering works"""
        rv = register(self, 'user1', 'default')
        assert b'Your account waits for approval.' in rv.data
        rv = register(, '', 'default')
        assert b'You have to enter a first_name' in rv.data
        rv = register(self, 'meh', '')
        assert b'You have to enter a last_name' in rv.data
        rv = register(self, 'user1', 'default', 'admin@mail.com')
        assert b'The email is already taken.' in rv.data
        rv = register(self, 'meh', 'foo', email='broken')
        assert b'You have to enter a valid email address' in rv.data 
        rv = register(self, 'meh', 'beh', 'meh@mail.com', '',)
        assert b'You have to enter a password' in rv.data
        rv = register(self, 'meh', 'beh', 'meh@mail', '1234hello', '1234hey')
        assert b'The two passwords do not match' in rv.data
        
    def tearDown(self):
        self.session.remove()


if __name__ == '__main__':
    unittest.main()

