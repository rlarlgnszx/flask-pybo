# --------------------------------- [edit] ---------------------------------- #
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
# --------------------------------- [edit] ---------------------------------- #
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email
# --------------------------------------------------------------------------- #
class QuestionForm(FlaskForm):
    # --------------------------------- [edit] ---------------------------------- #
    subject = StringField('제목', validators=[DataRequired('제목은 필수입력 항목입니다.')])
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
# --------------------------------------------------------------------------- #
# --------------------------------- [edit] ---------------------------------- #
class AnswerForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired('내용은 필수입력 항목입니다.')])
# -----------------------------s---------------------------------------------- #
# --------------------------------- [edit] ---------------------------------- #
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
# --------------------------------------------------------------------------- #
# --------------------------------- [edit] ---------------------------------- #
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])
# --------------------------------------------------------------------------- #
# --------------------------------- [edit] ---------------------------------- #
class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
# --------------------------------------------------------------------------- #