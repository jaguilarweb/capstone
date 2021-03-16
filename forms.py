from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SelectField, SelectMultipleField, DateTimeField
from wtforms.validators import InputRequired, NumberRange, DataRequired, AnyOf, URL


class ProjectForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    kind = StringField(
        'kind', validators=[DataRequired()]
    )
    deadline = DateTimeField(
        'deadline',
        validators=[DataRequired()]
    )
    person_id = SelectField(
        'person_id', choices=[], coerce=int, validate_choice=False, validators=[InputRequired()]
    )
    service_id = SelectField(
        'service_id', choices=[], coerce=int, validate_choice=False, validators=[InputRequired()]
    )


class ProjectEditForm(FlaskForm):
    deadline = DateTimeField(
        'deadline',
        validators=[DataRequired()]
    )
    word_count = IntegerField(
        'word_count'
    )
    hour_count = DecimalField(
        'hour_count'
    )
    rate = DecimalField(
        'rate'
    )


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


class ServiceForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired()]
    )
    source = StringField(
        'source', validators=[DataRequired()]
    )
    destiny = StringField(
        'destiny', validators=[DataRequired()]
    )
