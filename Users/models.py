import uuid
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from datetime import date

# Creating a validator function
def isPhoneNumber(value):
    if len(value) == 10:
        return value
    else:
        raise ValidationError("Phone number must have only 10 digits")

def isValidDate(value):
    today = date.today()
    if today == value:
        raise ValidationError("Invalid date")
    else:
        return value
    
class Address(models.Model):
    city = models.CharField(max_length=50 , null=True)
    state = models.CharField(max_length=50 , null=True)
    country = models.CharField(max_length=50 , null=True)
    code = models.CharField(max_length=6 , null=True)

# Users class inheriting models.Model
class Users(models.Model):
    _id = models.AutoField(auto_created=True, primary_key=True)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    DOB = models.DateField(
        null=True,
        validators=[isValidDate]
    )
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    password = models.CharField(
        null=True,
        max_length = 10000
    )
    passwordReSetId = models.UUIDField(null=True)
    currentActiveOrganization = models.IntegerField(null=True)
    email = models.EmailField(
        unique=True,
        error_messages={
            "unique": "User with this email is already exist",
            'invalid': 'Please enter a valid email address.'
        },
        validators=[EmailValidator()],
        db_index=True
    )
    phoneNumber = models.CharField(max_length=10,
                                   unique=True,
                                   null=True,
                                   error_messages={
                                       "unique": "User with this phone number is already exist",
                                       "max_length": "Phone number must have only 10 digits",
                                   },
                                   validators=[isPhoneNumber]
                                   )
    slug = models.SlugField(default="" , null=False , blank=True , db_index=True )
    address = models.ForeignKey(Address , on_delete=models.SET_NULL, null=True)

    def save(self , *args , **kwargs):
        slug = f"{self.firstName} {self.middleName} {self.lastName} {uuid.uuid4() }"
        print(slug)
        self.slug = slugify(slug)
        super().save(*args , **kwargs)

    def get_absolute_url(self):
        return reverse("user-detail" , [self._id])

    def __str__(self):
        return f"{self.firstName} {self.middleName} {self.lastName} ({self.email}) {self._id}"