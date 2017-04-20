from flask_wtf import FlaskForm #Em algumas versões é utlizado FlaskForm ao inves de Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired

class LeadForm(FlaskForm):
	name = StringField("name", validators=[DataRequired()])
	telnumber = StringField("telnumber", validators=[DataRequired()])
	email = StringField("email", validators=[DataRequired()])
