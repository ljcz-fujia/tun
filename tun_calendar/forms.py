from django import forms
from .models import UserRecord

# 用户记录表单
class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['record_type', 'event_info', 'event_time', 'period_type', 'period', 'reminder_threshold']
        widgets = {
            'record_type': forms.TextInput(attrs={'autocomplete': 'off'}),
            'event_info': forms.TextInput(attrs={'autocomplete': 'off'}),
            'event_time': forms.DateTimeInput(attrs={'autocomplete': 'off', 'type': 'datetime-local'}),
            'period_type': forms.Select(choices=[('公历', '公历'), ('农历', '农历')]),
            'period': forms.TextInput(attrs={'autocomplete': 'off'}),
            'reminder_threshold': forms.TextInput(attrs={'value': '0', 'autocomplete': 'off'}),
        }