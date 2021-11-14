from django.db import models

# Create your models here.

class Addresses(models.Model):
    # 모델이 가지고 있는 컬럼을 명시(스키마 정의)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=13)
    addresses = models.TextField()

    class Meta:
        ordering = ['created']

