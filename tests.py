import unittest
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

import models


class RolesModelTestCase(unittest.TestCase):

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
                            last_name='Doe', email='johndoe@mail.com')
        self.session.add(client1)
        self.session.commit()
        manager1 = models.Manager(
                                id=1, username='Helper')
        
    def test_clients_model(self):
        clients = self.session.query(models.Client).all()
        assert len(clients) == 1

    def tearDown(self):
        self.session.remove()


if __name__ == '__main__':
    unittest.main()

