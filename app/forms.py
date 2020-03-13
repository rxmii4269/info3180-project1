from flask_wtf import FlaskForm
from wtforms import StringField , TextAreaField, TextField , SelectField
from flask_wtf.file import FileField,FileRequired,FileAllowed
from wtforms.validators import DataRequired, Email , InputRequired




class ProfileForm(FlaskForm):
    mychoices = [('Male','Male'),('Female','Female')]
    firstname = TextField('First Name', validators=[DataRequired(),InputRequired()])
    lastname = TextField('Last Name',validators=[DataRequired(),InputRequired()])
    email = TextField('Email Address',validators=[DataRequired(),Email()])
    location = TextField('Location',validators=[DataRequired(), InputRequired()])
    biography = TextAreaField('Biography',validators=[DataRequired()])
    gender = SelectField('Gender',choices=mychoices,validators=[DataRequired()])
    profile_pic = FileField('Browse...',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],'Images only!')])

