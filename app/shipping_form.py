from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,SelectField
from wtforms.validators import DataRequired
from map.map import map

class ShippingForm(FlaskForm):
    sender = StringField('Sender',validators=[DataRequired()])
    recipient = StringField('Recipient',validators=[DataRequired()])
    origin = SelectField('Origin', choices=list(map))
    destination = SelectField('Destination', choices=list(map))
    submit = SubmitField('Submit')