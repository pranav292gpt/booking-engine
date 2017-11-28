from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from Timestampedmodel import Timestampedmodel
from django.contrib.postgres.fields import ArrayField

#User model to replace Django's default User.
class User(AbstractBaseUser, Timestampedmodel):
    first_name = models.CharField(max_length=64, blank=True, null=True)
    last_name = models.CharField(max_length=64, blank=True, null=True)
    username = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    install_type_choices = (
        ("o", "Organic"),
        ("r", "Referral"),
        )

    #Refferal fields
    #Array field with list of all the users primary key referred by the user.
    refferals = ArrayField(models.IntegerField(), blank=True, null=True)

    #Integer field containing primart key of the user whose refferal code was used while creating account.
    reffered_by = models.IntegerField(blank=True, null=True)
   
    #Refferal code of the user which can be used for reffering other users.
    refferal_code = models.CharField(max_length=16,null=True)

    install_type = models.CharField(max_length=32, choices=install_type_choices, default='o')


    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __unicode__(self):
        return self.username
