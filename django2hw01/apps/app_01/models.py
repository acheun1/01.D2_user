from django.db import models

# 1. Create a new model called 'User' with the information above.
# 2. Successfully create and run the migration files
# 3. Using the shell...
#     1.Know how to retrieve all users.
#     2. Know how to get the last user.
#     3. Create a few records in the users
#     4. Know how to get the first user.
#     5. Know how to get the users sorted by their first name (order by first_name DESC)
#     6. Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
#     Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).
# (optional) Ninja:
# Find a way to validate the data coming in to the shell.  For example, make sure that "name" fields are a minimum length, "email" is a valid email, or that "email" doesn't already exist in the db.

# Create your models here.

class UserManager(models.Manager):
    pass

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

#from apps.app_01.models import User
# 1 User.objects.all()
# 2 User.objects.last()
# 3 
#   User.objects.create(first_name="first1", last_name="last1", email="first1@email.com", age=1)
# User.objects.create(first_name="first2", last_name="last2", email="first2@email.com", age=2)
# User.objects.create(first_name="first3", last_name="last3", email="first3@email.com", age=3)
# User.objects.create(first_name="first4", last_name="last4", email="first4@email.com", age=4)
# User.objects.create(first_name="first5", last_name="last5", email="first5@email.com", age=5)

# 4 User.objects.first()
# 5 User.objects.order_by("-first_name")
# 6 update1 = User.objects.get(id=3)
#   update1.last_name = "last3change"
#   update1.save()
#   User.objects.get(id=3).last_name
# 7 User.objects.get(id=4).delete()
# (1, {'app_01.User': 1})

# RESULTS:
# >>> User.objects.get(id=4).first_name
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
#   File "C:\Users\jarvis\Documents\CodingDojo\python_stack\hwdjango\py6env\lib\site-packages\django\db\models\manager.py", line 85, in manager_method
#     return getattr(self.get_queryset(), name)(*args, **kwargs)
#   File "C:\Users\jarvis\Documents\CodingDojo\python_stack\hwdjango\py6env\lib\site-packages\django\db\models\query.py", line 385, in get
#     self.model._meta.object_name
# apps.app_01.models.DoesNotExist: User matching query does not exist.


# Get the record of the user whose id is 3 and UPDATE the person's last_name to something else. Know how to do this directly in the console using .get and .save.
# #     Know how to delete a record of a user whose id is 4 (use something like User.objects.get(id=2).delete...).