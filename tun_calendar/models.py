from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# 定义用户记录模型
class UserRecord(models.Model):
    # 关联用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 类型字段
    record_type = models.CharField(max_length=100)
    # 事件信息字段
    event_info = models.TextField()
    # 事件时间字段，默认为当前时间
    event_time = models.DateTimeField(null=True, blank=True)
    # 周期字段
    period = models.CharField(max_length=100)
    # 距离事件天数字段
    days_until_event = models.IntegerField()

    def __str__(self):
        return self.event_info