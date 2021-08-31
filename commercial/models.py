from django.db import models

# Create your models here.


class Counseling(models.Model):
    name = models.CharField(max_length=30, verbose_name="신청자 이름")
    phone_number = models.CharField(max_length=15, verbose_name="연락처")
    relation = models.CharField(max_length=20, verbose_name="어르신과의 관계")
    information = models.TextField(blank=False, verbose_name="어르신 상태")
    complete = models.BooleanField(default=False, verbose_name="상담완료 여부")
