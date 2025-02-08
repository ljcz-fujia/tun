from django import forms
from .models import UserRecord

# 用户记录表单
class UserRecordForm(forms.ModelForm):
    class Meta:
        model = UserRecord
        fields = ['record_type', 'event_info', 'event_time', 'period', 'days_until_event']