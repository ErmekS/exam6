from django import forms
from django.forms import widgets


class GuestbookForm(forms.Form):
    author = forms.CharField(max_length=20, required=True, label='Имя автора')
    email = forms.EmailField(empty_value=True, required=True, label='Email автора')
    entry = forms.CharField(max_length=2000, required=True, label='Entry', widget=widgets.Textarea(attrs={"cols": 40, "rows": 3}))
