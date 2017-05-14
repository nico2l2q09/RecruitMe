from django import forms
import datetime
from signup.models import Coach, Player
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.layout import Layout
from crispy_forms.bootstrap import InlineField
class CoachSignup(forms.ModelForm):
	school = forms.CharField(label='School', max_length=200)
	head_coach = forms.CharField(max_length=100, required=False)
	assistant_coach = forms.CharField(max_length=100, required=False)
	league = forms.CharField(max_length=100, required=False)
	phone = forms.CharField(label='Phone Number', max_length=50, required=False)
	photo = forms.ImageField(required=False, label='Upload a Profile Photo')
	#logo = forms.ImageField(required=False, label="logo")


	class Meta:
		model = Coach
		fields = ['school', 'head_coach', 'assistant_coach', 'league', 'phone', 'photo']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""
	
class PlayerSignup(forms.ModelForm):
	POSITION_CHOICES = (('Goalkeeper', 'Goalkeeper'),
						('Midfield', 'Midfield'),
						('Forward', 'Forward'),
						('Defense', 'Defense'))
	name = forms.CharField(label='Full Name', max_length=75)
	city = forms.CharField(label='City', max_length=100)
	club = forms.CharField(label='Club Team', max_length=100)
	state = forms.CharField(label='State', max_length=100)
	school = forms.CharField(label='School', max_length=100)
	position = forms.ChoiceField(label='Position', choices=POSITION_CHOICES)
	phone = forms.CharField(label='Club Coach Contact Number', max_length=100)
	SAT = forms.IntegerField(label='SAT')
	ACT = forms.IntegerField(label='ACT')
	GPA = forms.DecimalField(label='GPA', max_digits=3, decimal_places=2)
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=300)
	#achievements = forms.CharField(required=False, label='Achievements', max_length=500)
	photo = forms.ImageField(required=False, label='Upload a Profile Photo')

	#video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	class Meta:
		model = Player
		fields = ['name', 'club', 'city', 'state', 'school', 'position', 'SAT', 'ACT', 'GPA', 'phone', 'birthDate', 'video', 'photo']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'

	"""
class position(forms.Form):
	POSITION_CHOICES = (('All', 'All'),
						('Goalkeeper', 'Goalkeeper'),
						('Midfield', 'Midfield'),
						('Forward', 'Forward'),
						('Defense', 'Defense'))
	position = forms.ChoiceField(label='Position', choices=POSITION_CHOICES)
	gpa = forms.DecimalField(label='Minimum GPA', max_digits=3, decimal_places=2, required=False)
	sat = forms.IntegerField(label='Minimum SAT score', required=False)
	act = forms.IntegerField(label='Minimum ACT score', required=False)



class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email')

class UpdatePlayerProfile(forms.ModelForm):
	name = forms.CharField(label='Full Name', max_length=100, required=False)
	city = forms.CharField(label='City', max_length=100, required=False)
	club = forms.CharField(label='Club Team', max_length=100, required=False)
	state = forms.CharField(label='State', max_length=100, required=False)
	school = forms.CharField(label='School', max_length=100, required=False)
	position = forms.CharField(label='Position', max_length=100, required=False)
	phone = forms.CharField(label='Phone Number', max_length=100, required=False)
	SAT = forms.IntegerField(label='SAT', required=False)
	ACT = forms.IntegerField(label='ACT', required=False)
	GPA = forms.DecimalField(label='GPA', max_digits=3, decimal_places=2, required=False)
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	#achievements = forms.CharField(required=False, label='Achievements', max_length=500)
	photo = forms.ImageField(required=False, label='Upload a Profile Photo')

	#video = forms.CharField(required=False, label='Link To Highlight Video', max_length=150)
	class Meta:
		model = Player
		fields = ['name', 'club', 'city', 'state', 'school', 'position', 'SAT', 'ACT', 'GPA', 'phone', 'birthDate', 'video', 'photo']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""
class UpdateCoachProfile(forms.ModelForm):
	school = forms.CharField(label='School', max_length=100)
	head_coach = forms.CharField(max_length=100, required=False)
	assistant_coach = forms.CharField(max_length=100, required=False)
	league = forms.CharField(max_length=100, required=False)
	phone = forms.CharField(label='Phone Number', max_length=100, required=False)
	photo = forms.ImageField(required=False, label='Upload a Profile Photo')
	#logo = forms.ImageField(required=False, label="logo")


	class Meta:
		model = Coach
		fields = ['school', 'head_coach', 'assistant_coach', 'league', 'phone', 'photo']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'
	"""

