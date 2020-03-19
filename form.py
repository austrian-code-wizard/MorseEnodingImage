from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class InputForm(FlaskForm):
    text = TextAreaField('Input Text', validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 12})
    height = IntegerField('Image Height', validators=[DataRequired()])
    length = IntegerField('Image Length', validators=[DataRequired()])
    bit_length = IntegerField('Length per Data Unit', validators=[DataRequired()])
    stroke = IntegerField('Stroke Width', validators=[DataRequired()])
    spacing = IntegerField('Spacing', validators=[DataRequired()])
    submit = SubmitField('Create Encoding')
