from django import forms
from diy_users.models import DIYUsers


class UserForms(forms.ModelForm):

    class Meta:

        model = DIYUsers

        fields = [
            "first_name",
            "last_name",
            "avatar"
        ]

        # Customize the rendered HTML
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}),
            "last_name": forms.TextInput(attrs={'class': ' input', 'placeholder': 'Last Name'}),
            "phone_number": forms.TextInput(attrs={'id': 'phNumber', 'class': ' input', 'placeholder': '(555) 555-5555', 'type': 'tel', 'pattern': "^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$"}),
            "username": forms.TextInput(attrs={'class': 'input', 'placeholder': 'Username'}),
            "password": forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Password'}),
            "avatar": forms.FileInput(attrs={'class': 'control file has-name is-right'}),
            "email": forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email', 'type': 'email'}),
        }


class UserAuthorizeForm(UserForms):

    class Meta(UserForms.Meta):

        fields = [
            "username",
            "password",
        ]


class UserCreationsForm(UserForms):

    re_password = forms.CharField(max_length=40,
                                  widget=forms.PasswordInput(attrs={
                                      'autocomplete': 'new-password',
                                      'class': 'input',
                                      'placeholder': 'Password'
                                  }))

    def clean(self):
        cleaned_data = super(UserCreationsForm, self).clean()
        password = cleaned_data.get("password")
        re_password = cleaned_data.get("re_password")

        if password != re_password:
            self.add_error("re_password", "Passwords do not match!")

        return cleaned_data

    class Meta(UserForms.Meta):

        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "phone_number",
            "password",
            "re_password",
        ]
