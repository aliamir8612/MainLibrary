from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserExtend(AbstractUser):
    mobile_text = models.CharField('موبایل', max_length=11, blank = False)
    ncode_text = models.CharField('کد ملی', max_length=10, blank = False)
    mobile_status = models.BooleanField('وضعیت تایید موبایل', default= False, blank=False)
    email_status = models.BooleanField('وضعیت تایید ایمیل', default= False, blank=False)
    is_admin = models.BooleanField(default= False, blank=False)
    credit = models.DecimalField('اعتبار', default=10000000, blank=True, max_digits = 10, decimal_places = 0)
