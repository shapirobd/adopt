from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField
from wtforms.validators import InputRequired, URL, Optional

ages = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
        17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]


class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[
                       InputRequired(message="Pet Name can't be blank")])
    species = SelectField('Species', choices=[
        ("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = SelectField('Age', choices=[(age, age) for age in ages])
    notes = StringField('Notes')


class EditPetForm(FlaskForm):
    photo_url = StringField('Photo URL', validators=[URL()])
    notes = StringField('Notes')
    available = BooleanField('Is this pet available?')
