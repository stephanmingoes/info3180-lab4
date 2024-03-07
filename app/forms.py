from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired, FileRequired, FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])



class UploadForm(FlaskForm):
    file = FileField('Image File', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])