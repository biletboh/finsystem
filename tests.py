import unittest
import tempfile
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import finapp
import models
import testconfig

from finapp import create_app, db
from forms import RegisterForm 


class RolesModelTestCase(unittest.TestCase):
    """Test Project models."""
    
    def create_app(self):
        return create_app(self)

    def setUp(self):
        app = create_app(testconfig)
        with app.app_context():
            db.create_all() 

        client1 = models.Client(
                            id=1, first_name='John',
                            last_name='Doe', email='johndoe@mail.com',
                            passport_number='AB2340923', password='123asdf',
                            balance=0)
        db.session.add(client1)

        to_approve1 = models.ApprovalList(
                                id=1, first_name='John',
                                last_name='Doe', email='johndoe@mail.com',
                                passport_number='AB2340923')
        db.session.add(to_approve1)

        manager1 = models.Manager(
                                id=1, username='Helper', password='123asdf')
        print(models.Client.query.all())
        db.session.add(manager1)

        db.session.commit()

        
    def test_client_model(self):
        clients = db.session.query(models.Client).all()
        assert len(clients) == 1

    def test_manager_model(self):
        managers = db.session.query(models.Manager).all()
        assert len(managers) == 1

    def tearDown(self):
        db.session.remove()
        db.drop_all()


#class RegisterEndpointTestCase(unittest.TestCase):
#    """Test register endpoint."""
#
#    def create_app(self):
#        app = app
#        app.config['TESTING'] = True
#        app.config['WTF_CSRF_ENABLED'] = False
#        return app
#
#    def setUp(self):
#
#        db.create_all()
#
#        client1 = models.Client(
#                            id=1, first_name='John',
#                            last_name='Doe', email='johndoe@mail.com',
#                            passport_number='AA000000', password='123asdf',
#                            balance=0)
#        db.session.add(client1)
#        db.session.commit()
# 
#    def tearDown(self):
#        Base.query = db.session.query_property()
#        print('metadata', Base.metadata)
#        db.session.remove()
#
#    def register(
#                self, first_name, last_name, email,
#                passport_number):
#        """Use helper function to register a user."""
#        
#        if email is None:
#            email = username + '@example.com'
#        return self.app.post('/register', data={
#                                            'first_name': first_name,
#                                            'last_name': last_name,
#                                            'email': email,
#                                            'passport_number': passport_number,
#                                            }, follow_redirects=True)
#
#        
#    def test_register_endpoint(self):
#        """Make sure registering works."""
##        rv = self.register('user1', 'default', 'snewmail@mail.com', 'AA9090909')
##        assert b'Your account waits for approval.' in rv.data
#        rv = self.register('', 'default', 'meh@mail.com', '1234hello')
#        assert b'You have to enter a first_name.' in rv.data
#        rv = self.register('meho', '', 'meh@mail.com', '1234hello')
#        assert b'You have to enter a last_name.' in rv.data
#        rv = self.register('ola', 'default', '', '1234hello')
#        assert b'You have to enter an email.' in rv.data
#        rv = self.register('meh', 'foo', 'broken', '1234hello')
#        assert b'You have to enter a valid email address' in rv.data
#        rv = self.register('user1', 'default', 'johndoe@mail.com', 'AA000000')
#        assert b'The email is already taken.' in rv.data
#        rv = self.register('meh', 'beh', 'meh@mail.com', '')
#        assert b'You have to enter a passport_number' in rv.data
#        rv = self.register('user1', 'default', 'meh@mail.com', 'AA000000')
#        assert b'The passport number is already taken.' in rv.data
#
#
if __name__ == '__main__':
    unittest.main()

