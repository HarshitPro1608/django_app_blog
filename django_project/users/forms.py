#inherits from user creation form
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth. forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):#inherits from usercreation form
    email = forms.EmailField()#include email in forms
    class Meta:#keeps config at one place
        model = User#in user model we need to add these fields(email included)
        fields = ['username', 'email', 'password1', 'password2']
        
        
class UserUpdateForm(forms.ModelForm):#update user forms
    
    email = forms.EmailField()#include email in forms
    
    class Meta:#keeps config at one place
        model = User#in user model we need to add these fields(email included)
        fields = ['username', 'email']
        
class ProfileUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ['image']