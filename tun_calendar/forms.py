from django import forms
from .models import UserRecord

# 用户记录表单
class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['record_type', 'event_info', 'event_time', 'period']
        widgets = {
            'record_type': forms.TextInput(attrs={'autocomplete': 'off'}),
            'event_info': forms.TextInput(attrs={'autocomplete': 'off'}),
            'event_time': forms.DateTimeInput(attrs={'autocomplete': 'off', 'type': 'datetime-local'}),
            'period': forms.TextInput(attrs={'autocomplete': 'off'}),
        }