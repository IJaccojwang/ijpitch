from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField, SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch title', validators = [Required()])
    description = StringField('Pitch description', validators = [Required()])
    category = category = SelectField('Select category', choices=[('pickup', 'Pick Up Lines'), ('product', 'Products'), ('business', 'Business')])
    review = TextAreaField('New Pitch')
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Pitch Comment', validators=[Required()])
    submit = SubmitField('Submit')