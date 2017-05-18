from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class RegisterForm(UserCreationForm):


    #Djangoデフォルトログインではusernameとpasswordでログインするため
    #今回はfirst_name をユーザーネームとして扱う
    #username = email　アドレスと考える
    #required = Trueで登録時必須にする
    first_name = forms.CharField(label="ユーザーネーム", required=True)

    class Meta:
        model = User
        fields = (
            "username","password1","password2",
            "email", "first_name",
        )



    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'メールアドレス'

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'ユーザーネーム'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'パスワード'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'パスワード（確認）'


    def clean_username(self):
        username = self.cleaned_data["username"]
        atmark = username.find('@')
        string = username.find("dendai.ac.jp")

        if(atmark < 0):
            raise ValidationError("正しいメールアドレスを指定してください。")

        if(atmark > string and string < 0):
            raise ValidationError("電大メールを入力してください")

        # try:
        #     validate_email(username)
        # except ValidationError:
        #     raise ValidationError("正しいメールアドレスを指定してください。")

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        else:
            raise ValidationError("既に存在するメールアドレスです。")


class LoginForm(AuthenticationForm):
    #ログインフォーム作成
    #username = email と考える

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'メールアドレス'

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'パスワード'