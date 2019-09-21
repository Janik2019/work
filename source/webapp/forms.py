from django import forms
from django.forms import widgets
# from webapp.models import status_choices


class guestbookForm(forms.Form):
    name = forms.CharField(max_length=50, required=True, label='Имя автора')
    email = forms.EmailField(max_length=20, required=True, label='Почтовый ящик')
    text = forms.CharField(max_length=3000, required=True, label='Текст', widget=widgets.Textarea)