from flask_security.utils import encrypt_password
from finapp import app, db
from security import user_datastore
from models import Role, Manager


#  Run this script to create roles and Superuser
def create_roles_and_superuser():
    with app.app_context():
        
        #  Create roles 
        sup_role = Role(
                    name='superuser', 
                    description='This user can create managers.'
                    )

        man_role = Role(
                    name='manager', 
                    description='Managers can approve client accounts')

        db.session.add(sup_role)
        db.session.add(man_role)
        db.session.commit()

        #  Customize your super user on production
        superuser = user_datastore.create_user(
                username='SuperManager', email='admin@mail.com',
                password=encrypt_password('superuserpass'),
                roles=[sup_role])

        db.session.commit()

        return

create_roles_and_superuser()

