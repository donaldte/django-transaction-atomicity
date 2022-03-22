from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    receiver = forms.CharField()
    class Meta:
        model = Account

        fields = "__all__"