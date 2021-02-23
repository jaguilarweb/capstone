from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import InputRequired, NumberRange, DataRequired, AnyOf, URL


class PersonForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    kind = StringField(
        'kind'
    )
    email = StringField(
        'email'
    )
    ratew = DecimalField(
        'ratew', validators=[InputRequired()]
    )
    rateh = DecimalField(
        'rateh', validators=[InputRequired()]
    )
    
   