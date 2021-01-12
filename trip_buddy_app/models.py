from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['form_password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if not EMAIL_REGEX.match(postData['form_email']):
            errors['email'] = "Invalid email"
        if len(postData['form_first_name']) < 2:
            errors['first_name'] = "First name is too short."
        if len(postData['form_last_name']) < 2:
            errors['last_name'] = "Last name is too short."
        if postData['form_password'] != postData['form_password_confirm']:
            errors['password'] = "Passwords do not match!"
        return errors
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            log_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), log_user.password.encode()):
                errors['password'] = "Invalid login."
        else:
            errors['password'] = "Invalid login attempt."
        return errors

# class TripManager(models.Manager):
#     def basic_validator(self, postData):
#         return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    plan = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    User = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # objects = TripManager()