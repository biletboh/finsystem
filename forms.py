from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

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
                        'Last Name',
                        [DataRequired(message='The email is already taken.')],
                        [Email(
                            message='You have to enter a valid email address'
                            )]
                        )
    passport_number = StringField(
                                'Last Name',
                                [DataRequired(
                                    message='You have to enter a passport_number'
                                    )],

                                )

