from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Business, Profile

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        field = '__all__'
        exclude = ['user']

class BusinessForm(ModelForm):
    class Meta:
        model = Business
        field = '__all__'
        exclude = ['user']