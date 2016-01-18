from flask.ext.wtf import Form
from wtforms.fields import TextField, FileField, SelectField, SubmitField
# other fields include PasswordField
from wtforms.validators import Required, Email

class ProfileForm(Form):
    image = FileField('Image', validators=[Required()])
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    age = TextField('Age', validators=[Required()])
    sex = SelectField(u'Sex', choices=[('select', 'Select'), ('female', 'Female'), ('male', 'Male')])
    create = SubmitField('Create')