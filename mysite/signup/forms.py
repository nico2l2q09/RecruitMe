from django import forms
import datetime
from signup.models import Coach, Player
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import TabHolder, Tab
from django.forms.extras.widgets import SelectDateWidget
class CoachSignup(forms.ModelForm):
	first_name = forms.CharField(label='First Name', max_length=25)
	last_name = forms.CharField(label='Last Name', max_length=25)
	school = forms.CharField(label='School', max_length=25)
	phone = forms.CharField(label='Phone Number', max_length=25)
	email = forms.CharField(label='Email', max_length=25)
	class Meta:
		model = Coach
		fields = ['first_name', 'last_name', 'school', 'email', 'phone']
	"""helper = FormHelper()
	helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
	helper.form_method = 'POST'"""
	

class PlayerSignup(forms.ModelForm):
	first_name = forms.CharField(label='First Name', max_length=25)
	last_name = forms.CharField(label='Last Name', max_length=25)
	city = forms.CharField(label='City', max_length=25)
	state = forms.CharField(label='State', max_length=25)
	school = forms.CharField(label='School', max_length=25)
	position = forms.CharField(label='Position', max_length=25)
	email = forms.CharField(label='Email', max_length=25)
	phone = forms.CharField(label='Phone Number', max_length=25)
	SAT = forms.IntegerField(label='SAT')
	ACT = forms.IntegerField(label='ACT')
	birthDate = forms.DateField(label='Birth Date', widget=SelectDateWidget(years=range(1985, datetime.date.today().year+10)))
	class Meta:
		model = Player
		fields = ['first_name', 'last_name', 'city', 'state', 'school', 'position', 'SAT', 'ACT', 'email', 'phone', 'birthDate']
