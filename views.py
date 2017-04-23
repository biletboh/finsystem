from validate_email import validate_email
from flask import request, redirect, render_template, flash, \
    jsonify
from flask_restful import Resource
from flask_restful import reqparse
from models import Client, ApprovalList, Role
from finapp import app, db, api


def email(email_str):
    """Return email_str if valid, raise an exception in other case."""
    if validate_email(email_str):
        return email_str
    else:
        raise ValueError('{} is not a valid email'.format(email_str))


parser = reqparse.RequestParser()

parser.add_argument('first_name', required=True)
parser.add_argument('last_name', required=True)
parser.add_argument('email', type=email, required=True)
parser.add_argument('passport_number', required=True)


class RegisterClient(Resource):

    def get(self):
        return {'to register': 'client', 'post': 'fist_name, last_name, email, passport_number'}

    def post(self):
        args = parser.parse_args() 
        to_approve = ApprovalList(
                                first_name=args['first_name'],
                                last_name=args['last_name'], 
                                email=args['email'],
                                passport_number=args['passport_number'])

        db.session.add(to_approve)
        db.session.commit()
        client = to_approve.serialize
        return client, 201 
       
api.add_resource(RegisterClient, '/register')

