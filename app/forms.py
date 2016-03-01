from flask.ext.wtf import Form
from wtforms.fields import TextField, FileField, SelectField, SubmitField, IntegerField

from wtforms.validators import Required, Email, Length, NumberRange

class ProfileForm(Form):
    image = FileField('Image', validators=[Required(message="Please upload an image.")])
    firstname = TextField('Firstname', validators=[Required(message="Please enter your first name."),\
     	Length(min=2, max=80, message="Must be at least 2 and at most 80 characters in length.")])
    lastname = TextField('Lastname', validators=[Required(message="Please enter your last name."),\
    	Length(min=2, max=80, message="Must be at least 2 and at most 80 characters in length.")])
    age = IntegerField('Age', validators=[Required(message="Please enter your age."), NumberRange(min=10, message="You must be at least 10 years old to create a profile.")])
    sex = SelectField(u'Sex', choices=[('select', 'Select'), ('female', 'Female'), ('male', 'Male')])
    create = SubmitField('Create')