from django.contrib.auth.forms import UserCreationForm,forms
from django.contrib.auth.models import User

# class UserSignUpForm(UserCreationForm):
#     email = forms.EmailField()
#     university = forms.CharField()
#     department = forms.CharField()
#     experience = forms.IntegerField()
#     location = forms.ChoiceField()
#     contact = forms.CharField()
#
#     class Meta:
#         model = User
#         fields = [
#             'username',
#             'email',
#             'university',
#             'department',
#             'experience',
#             'location',
#             'contact',
#             'password1',
#             'password2',
#         ]


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    address = forms.CharField()
    contact = forms.CharField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
            'address',
            'contact',
        ]