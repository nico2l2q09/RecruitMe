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
	head_coach = forms.CharField(max_length=50, required=False)
	assistant_coach = forms.CharField(max_length=50, required=False)
	league = forms.CharField(max_length=25, required=False)
	phone = forms.CharField(label='Phone Number', max_length=25, required=False)
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	photo = forms.ImageField(required=False, label='Upload a Profile Photo')
	#logo = forms.ImageField(required=False, label="logo")


	class Meta:
		model = Coach
		fields = ['school', 'head_coach', 'assistant_coach', 'league', 'phone', 'video', 'photo']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""
	
class PlayerSignup(forms.ModelForm):
	city = forms.CharField(label='City', max_length=50)
	club = forms.CharField(label='Club Team', max_length=50)
	state = forms.CharField(label='State', max_length=50)
	school = forms.CharField(label='School', max_length=50)
	position = forms.CharField(label='Position', max_length=50)
	phone = forms.CharField(label='Phone Number', max_length=40)
	SAT = forms.IntegerField(label='SAT')
	ACT = forms.IntegerField(label='ACT')
	GPA = forms.DecimalField(label='GPA', max_digits=3, decimal_places=2)
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	achievements = forms.CharField(required=False, label='Achievements', max_length=500)
	#video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	class Meta:
		model = Player
		fields = ['club', 'city', 'state', 'school', 'position', 'SAT', 'ACT', 'GPA', 'phone', 'birthDate', 'video', 'achievements']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name','username', 'email')