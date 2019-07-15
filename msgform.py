from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL

# A class to validate the data given through the user-input
#title, sender and content are strings
#with minimum size of four-ten letters/characters and and maximum of 35 and 100 letters/characters
#URl input is validated using url()

class MessageForm(FlaskForm):
    title = StringField('Title',
                        validators=[DataRequired(), Length(min=4, max=35)])
    sender = StringField('Sender',
                         validators=[DataRequired(), Length(min=4, max=35)])
    content = StringField('Content ',
                          validators=[DataRequired(), Length(min=10, max=100)])
    url = StringField('URL ',
                      validators=[DataRequired(), URL()])

    submit = SubmitField('Send')


