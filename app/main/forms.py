from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Post title', validators = [Required()])
    message = TextAreaField('Blog post', validators = [Required()], render_kw={'class': 'form-control', 'rows': 20})
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('profile.',validators = [Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Comment on the blog:',validators=[Required()])
    submit = SubmitField('Submit')
