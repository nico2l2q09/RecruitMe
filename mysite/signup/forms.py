from django import forms
import datetime
from signup.models import Coach, Player
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CoachSignup(forms.ModelForm):
	school = forms.CharField(label='School', max_length=25)
	head_coach = forms.CharField(max_length=50)
	assistant_coach = forms.CharField(max_length=50)
	league = forms.CharField(max_length=25)
	phone = forms.CharField(label='Phone Number', max_length=25)
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)

	#logo = forms.ImageField(required=False, label="logo")


	class Meta:
		model = Coach
		fields = ['school', 'head_coach', 'assistant_coach', 'league', 'phone', 'video']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""
	

class PlayerSignup(forms.ModelForm):
	city = forms.CharField(label='City', max_length=25)
	state = forms.CharField(label='State', max_length=25)
	school = forms.CharField(label='School', max_length=25)
	position = forms.CharField(label='Position', max_length=25)
	phone = forms.CharField(label='Phone Number', max_length=25)
	SAT = forms.IntegerField(label='SAT')
	ACT = forms.IntegerField(label='ACT')
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	#video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	class Meta:
		model = Player
		fields = ['city', 'state', 'school', 'position', 'SAT', 'ACT','phone', 'birthDate', 'video']
	
class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email')