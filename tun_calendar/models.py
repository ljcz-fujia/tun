from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from dateutil.relativedelta import relativedelta

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

    def __str__(self):
        return self.event_info

    def calculate_days_until_event(self):
        # 确保 event_time 是带时区的日期时间对象
        if self.event_time and timezone.is_naive(self.event_time):
            event_time = timezone.make_aware(self.event_time)
        else:
            event_time = self.event_time

        # 获取当前带时区的日期时间
        now = timezone.now()

        # 计算距离目标日期的天数
        days_diff = (event_time.date() - now.date()).days
        return days_diff