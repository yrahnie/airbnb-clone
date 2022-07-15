from django import forms
from django.contrib.auth.forms import UserCreationForm

from . import models


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    # field 의 값을 확인하고자 할 때 clean_field-name 형태로 함수를 만들어야 함.
    # 이후 data 는 form.cleaned_data 로 확인 가능. return 해주지 않으면 NULL 값이 확인됨.
    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     print("print = ", email)
    #     try:
    #         models.User.objects.get(
    #             username=email
    #         )
    #         return email
    #     except models.User.DoesNotExist:
    #         raise forms.ValidationError("User does not exist")

    # 두 개의 다른 field 가 서로 관련이 있을 때 확인하는 method는 그냥 clean()
    def clean(self):
        email = self.cleaned_data.get("email")  # user가 보낸 데이터에서 email 을 가져옴
        password = self.cleaned_data.get("password")
        try:
            # User 모델에서 동일한 email 을 가진 user 가 있는지 찾음.
            user = models.User.objects.get(email=email)
            if user.check_password(password):
                return self.cleaned_data  # clean() 에서는 valid 할 경우 항상 이렇게 return 해줘야 함.
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


# ModelForm: Model 에 연결된 Form
# form 을 만들면 django 는 어떤 model 을 만들고 싶어하는지 암.
# clean() method 를 통한 validate 을 따로 할 필요가 없음. (model 에 있는 필드라면. 없는 필드라면 validate 해야함)
# 일반 Form 에는 없는 save() method 가 있음. override 가능.
class SignUpForm(UserCreationForm):
    username = forms.EmailField(label="Email")
