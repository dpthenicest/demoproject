from django import forms
from django.forms.widgets import NumberInput

from .models import Logger

FAVORITE_DISH = (
  ('italian', 'Italian'),
  ('greek', 'Greek'),
  ('turkish', 'Turkish'),
)

SHIFTS = (
  ("1", "Morning"),
  ("2", "Afternoon"),
  ("3", "Evening"),
)

class DemoForm(forms.Form):
  name = forms.CharField(widget=forms.Textarea(attrs={'rows': 5}))
  email = forms.EmailField(label="Enter email address")
  reservation_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
  favorite_dish = forms.ChoiceField(choices=FAVORITE_DISH)

class InputForm(forms.Form):
  first_name = forms.CharField(max_length=200)
  last_name = forms.CharField(max_length=200)
  shift = forms.ChoiceField(choices=SHIFTS)
  time_log = forms.TimeField(help_text="Enter an accurate time!")

class LogForm(forms.ModelForm):
  class Meta:
    model = Logger
    fields = '__all__'