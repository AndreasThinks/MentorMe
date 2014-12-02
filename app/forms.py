from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, IntegerField
from wtforms.validators import Required, length

class NewMentor(Form):
    first_name = TextField('First Name', validators = [Required()])
    last_name = TextField('Last Name', validators = [Required()])
    email = TextField('Email', validators = [Required()])
    phone_no = IntegerField('Phone Number')
    password = PasswordField('Password', validators = [Required()])
    title = TextField('Job Title', validators = [Required()])
    rank = TextField('Rank', validators = [Required()])
    ocu = TextField('OCU / Division', validators = [Required()])
    specialisations = TextField('Specialisations', validators = [Required()])
    cv = TextField('CV', validators = [Required()])
    phone = IntegerField('Phone Chat')
    mentor = BooleanField('Mentor')
    coffee = BooleanField('Coffee')
    phone_chat = BooleanField('Phone Chat')
    email_chat = BooleanField('Email Chat')

    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        super(NewMentor, self).__init__(*args, **kwargs)