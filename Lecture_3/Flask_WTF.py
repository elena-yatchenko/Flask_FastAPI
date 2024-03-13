"""
Чтобы упростить доступ к форме входа, базовый шаблон должен включать в себя ссылку на панель навигации:
<div>
    Microblog:
    <a href="/index">Home</a>
    <a href="/login">Login</a>
</div>"""

"""
Метод validate_<fieldname> в качестве валидатора поля формы.
Чтобы обеспечить настраиваемую проверку/валидацию, для каждого поля формы можно определить метод с именем validate_<fieldname>, где fieldname - это имя поля:

class SignupForm(Form):
    age = IntegerField('Age')

    def validate_age(form, field):
        if field.data < 13:
            raise ValidationError("We're sorry, you must be 13 or older to register")
"""
