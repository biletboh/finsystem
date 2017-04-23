from flask import Flask, request, redirect, render_template, flash, \
    jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from models import Base, Client, ApprovalList, Role
from forms import RegisterForm


# Create application
app = Flask(__name__)


app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key',
    WTF_CSRF_SECRET_KEY='secret csrf key',
    ))

engine = create_engine('sqlite:///roles.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(Base, Client, Role)
security = Security(app, user_datastore, register_form=RegisterForm)


@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def RegisterClient():
    form = RegisterForm()

    if form.validate_on_submit():
        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        passport_number = form.passport_number.data
        to_approve = ApprovalList(
                                first_name=first_name,
                                last_name=last_name, 
                                email=email,
                                passport_number=passport_number)

        session.add(to_approve)
        session.commit()

        return jsonify(ApprovalList=to_approve.serialize)

    print(dir(Client))    
    # Add basic template with form context to make tests work
    return render_template('customregister.html', form=form)


@app.route('/success', methods=['GET'])
def WaitForApproval():
    return 'Your account waits for approval.'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

