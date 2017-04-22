from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

from models import Client


class RegisterForm(FlaskForm):
    first_name = StringField(
                        'First Name',
                        [DataRequired(
                                    message='You have to enter a first_name.'
                                    )]
                        )
    last_name = StringField(
                        'Last Name', 
                        [DataRequired(
                                    message='You have to enter a last_name.'
                                    )]
                        )
    email = StringField(
                        'Email',
                        [
                        DataRequired(message='You have to enter an email.'),
                        Email(
                            message='You have to enter a valid email address'
                            )],
                        )
    passport_number = StringField(
                                'Passport',
                                [DataRequired(
                                    message='You have to enter a passport_number'
                                    )],
                                )

    def validate(self):
        rv = FlaskForm.validate(self)
        if not rv:
            return False

        client = Client.query.filter_by(email=self.email.data).first()
        if not client is None:
            self.email.errors.append('The email is already taken.')
            return False

        client = Client.query.filter_by(
                            passport_number=self.passport_number.data).first()
        if not client is None:
            self.passport_number.errors.append(
                                    'The passport number is already taken.')
            return False

        return True

