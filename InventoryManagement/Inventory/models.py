from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from rest_framework.authtoken.models import Token


class CustomAccountManager(BaseUserManager):
    def create_user(self, email,  password):
        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email,  password=password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        Token.objects.create(user=user)
        return user

    def get_by_natural_key(self, email_):

        return self.get(email=email_)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    employee_id = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=13, null=False)
    created_on = models.DateTimeField(auto_now_add=True)
    must_change_password = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'Login'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    role_type = models.CharField(max_length=100)
    level = models.CharField(max_length=100)


class Inventory(models.Model):
    id = models.IntegerField(primary_key=True)
    product_type = models.CharField(max_length=500)


class Status(models.Model):
    id = models.IntegerField(primary_key=True)
    status_type = models.CharField(max_length=100)


class Designations(models.Model):
    id = models.IntegerField(primary_key=True)
    designation_type = models.CharField(max_length=200)
    designation_id = models.CharField(max_length=100)

