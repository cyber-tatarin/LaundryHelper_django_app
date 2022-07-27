from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Profile

User = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'username']


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                            'id': "profile-name",
                                            'aria-describedby': "nameHelp"})
        }
