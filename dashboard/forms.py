from django import forms
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    username = forms.CharField(min_length=10, max_length=15, required=True)
    first_name = forms.CharField(min_length=1, required=True)
    last_name = forms.CharField(min_length=2, required=True)
    password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)
    confirm_password = forms.CharField(min_length=8, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']

    def clean(self):
        cleaned_data = super(SignupForm, self).clean()
        password = cleaned_data['password']
        confirm_password = cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match!')