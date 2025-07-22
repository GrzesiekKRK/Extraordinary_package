from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    # phone_number = forms.CharField(max_length=11)
    # secondary_email = forms.EmailField(max_length=50, null=True, blank=True)
    # billing_address = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "secondary_email",
            "billing_address",
            "phone_number",
            "postal_code",
        )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    phone_number= forms.CharField(
        max_length=25,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    secondary_email = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    billing_address = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "phone_number",
            "secondary_email",
            "billing_address",
            "postal_code",
        )
