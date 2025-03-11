# slicni modelima, kreiramo klase koje imaju polja u kojima unosimo podatke u vidu formi u nasim templatima

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists!')
        
    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists!')

    username = StringField(label='User name', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()]) # druga lozinka je za potvrdjivanje lozinke
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Sign In')

class PurchaseItemForm(FlaskForm):
    submit = SubmitField(label='Yes')

class SellItemForm(FlaskForm):
    submit = SubmitField(label='Sell Item')

class ContactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    message = StringField(label='Message')
    submit = SubmitField(label='Submit')
