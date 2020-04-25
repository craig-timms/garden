# blog_posts/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField,IntegerField,FloatField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    text = TextAreaField('Text',validators=[DataRequired()])
    submit = SubmitField("Post")

class BeerEntryForm(FlaskForm):
    man = StringField('Man',validators=[DataRequired()])
    model = StringField('Model',validators=[DataRequired()])
    alc = StringField('Alc',validators=[DataRequired()])
    volume = StringField('Volume',validators=[DataRequired()])
    quantity = StringField('Quantity',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    submit = SubmitField("Submit")
