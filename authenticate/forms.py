from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password',)


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'placeholder':'Email Addres', 'required':'true', 'id': 'inputEmail', 'type':'email'}), )
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder':'First Name', 'required':'true', 'id': 'firstname', 'type':'text'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'required':'true', 'id': 'inputLastName', 'type':'text'}))
	
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['id'] = 'inputUsername'
		self.fields['username'].widget.attrs['type'] = 'text'
		self.fields['username'].widget.attrs['name'] = 'username'
		self.fields['username'].widget.attrs['required'] = 'true'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
		self.fields['password1'].widget.attrs['id'] = 'inputNewPassword1'
		self.fields['password1'].widget.attrs['type'] = 'password'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = '' 		
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'	
		self.fields['password2'].widget.attrs['id'] = 'inputNewPassword2'
		self.fields['password2'].widget.attrs['type'] = 'password'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'