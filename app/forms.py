from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectField, TextField
from wtforms.validators import InputRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired

class PropertyForm(FlaskForm):
    title = StringField('title', validators=[InputRequired()])
    bedrooms = StringField('bedrooms', validators=[InputRequired()])
    bathrooms = StringField('bathrooms', validators=[InputRequired()])
    price = StringField('price', validators=[InputRequired()])
    location = StringField('Location', validators=[InputRequired()])
    type_ = SelectField ('type_', choices=[('house','House'), ('apartment','Apartment')])
    description= TextField('description', validators=[InputRequired()])
    photo = FileField ('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])