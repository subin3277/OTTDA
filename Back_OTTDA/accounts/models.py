from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, login_id, email, nickname, password, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            login_id=login_id,
            email=email,
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login_id=None, email=None, nickname=None, password=None, **extra_fields):
        superuser = self.create_user(
            login_id=login_id,
            email=email,
            nickname=nickname,
            password=password,
        )
        superuser.is_staff = True
        superuser.is_superuser = True
        superuser.is_active = True
        superuser.save(using=self._db)
        return superuser


class User(AbstractBaseUser, PermissionsMixin):
    login_id = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=20, unique=True, null=False, blank=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'login_id'
    REQUIRED_FIELDS = ['email', 'nickname']

    class Meta:
        db_table = 'user'
