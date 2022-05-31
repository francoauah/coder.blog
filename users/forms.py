from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile

class SignUpForm(UserCreationForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__( *args, **kwargs )

        self.fields ['username'].widget.attrs['class'] = 'form-control'
        self.fields ['password1'] . widget.attrs [ ' class ' ] = 'form-control'
        self.fields ['password2'] . widget.attrs [ ' class ' ] = 'form-control'

#-------------------------------------------------------------------------------------------------#

class EditProfileForm(UserChangeForm):
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    username= forms.CharField(max_length=100, widget= forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

#-------------------------------------------------------------------------------------------------#

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('biographie', 'profile_pic', 'twitter', 'facebook', 'website')

        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_pic':forms.(attrs={'class': 'form-control'}),
            'twitter':forms.TextInput(attrs={'class': 'form-control'}),
            'facebook':forms.TextInput(attrs={'class': 'form-control'}),
            'website':forms.TextInput(attrs={'class': 'form-control'}),
        }