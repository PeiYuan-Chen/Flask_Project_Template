from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    StringField,
    SelectMultipleField,
    SelectField,
    DateTimeField,
)
from wtforms.validators import DataRequired, Regexp, URL, Optional
from datetime import datetime


class MyForm(FlaskForm):
    string_field1 = StringField(
        label="string_field1",
        validators=[
            DataRequired(),
            Regexp(regex=r"^\d{3}$", message="field must be in the form of ..."),
        ],
    )
    string_field2 = StringField(
        label="string_field2",
        validators=[Optional(), URL()],
    )
    boolean_field = BooleanField(label="boolean_field")
    select_field = SelectField(
        label="select_field",
        validators=[DataRequired()],
        choices=[("C1", "C1"), ("C2", "C2")],
    )
    select_multiplefield = SelectMultipleField(
        label="select_multiplefield",
        validators=[DataRequired()],
        choices=[("C1", "C1"), ("C2", "C2")],
    )
    datatime_field = DateTimeField(
        label="datatime_field", validators=[DataRequired()], default=datetime.now()
    )
