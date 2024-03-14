from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    # birthday = DateField("Birthday")
    birthday = DateField("Birthday", format="d%.m%.Y%")
    agreement = BooleanField(
        "I agree with processing of my personal data", validators=[DataRequired()]
    )


"""Я писала с указанием формата и без этого атрибута, в обоих случаях в форме результат запрашивает как дд.мм.гггг,
а в принт выводит формат 1984-11-20. 

Подскажите, пожалуйста, как правильно все-таки оформлять это поле и как я могу в этом случае проверить соответствие формата, как запрашивается 
в задаче к примеру - (например, дата рождения должна быть в  формате дд.мм.гггг)"""
