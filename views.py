from flask import request, redirect, render_template, flash, \
    jsonify
from models import Client, ApprovalList, Role
from forms import RegisterForm
from finapp import app


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

    # Add basic template with form context to make tests work
    return render_template('customregister.html', form=form)


@app.route('/success', methods=['GET'])
def WaitForApproval():
    return 'Your account waits for approval.'

