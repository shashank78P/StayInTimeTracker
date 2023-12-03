import os
import uuid
from django.db import models
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.utils.text import slugify
from Users.models import Address, Users

# Create your models here.
class Organization(models.Model):
    _id = models.AutoField(auto_created=True, primary_key=True)
    name = models.CharField(
        unique=True,
        max_length=100,
        error_messages={
            "unique": "Organization name is already exist",
            'invalid': 'Please enter a valid organization name.'
        },
        db_index=True,
    )
    address = models.ForeignKey(Address , on_delete=models.SET_NULL, null=True)
    webSiteLink = models.CharField(max_length=2000)
    socialMediaLink = models.CharField(max_length=2000)
    contactEmail = models.EmailField(
        unique=True,
        error_messages={
            "unique": "This email is already exist",
            'invalid': 'Please enter a valid email address.'
        },
        validators=[EmailValidator()],
        db_index=True
    )
    logo = models.ImageField(
        upload_to="organizationLogo",
        default="organization.png",
        max_length=20000 , 
        error_messages={
            'invalid': 'Invalid file (file is not acceptable).'
        },
    )
    description = models.CharField(max_length=2000)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="" , null=False , blank=True , db_index=True )

    def save(self , *args , **kwargs):
        slug = f"{self.name} {uuid.uuid4() }"
        print(slug)
        self.slug = slugify(slug)
        super().save(*args , **kwargs)

    def __str__(self):
        return f"{self.name}"


class OwnerDetails(models.Model):
    OrganizationId =models.ForeignKey(Organization , on_delete=models.CASCADE, null=True)
    userId = models.ForeignKey(Users , on_delete=models.CASCADE, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.OrganizationId.name} ({self.userId.email})"
    
class Team(models.Model):
        name = models.CharField(max_length=100)
        checkInTime = models.TimeField()
        OrganizationId =models.ForeignKey(Organization, db_index=True , on_delete=models.CASCADE, null=True)
        checkOutTime = models.TimeField()
        description = models.CharField(
             max_length=2000,
             error_messages={
                  'invalid': 'Description is too long...'
            },
        )
        createdBy = models.ForeignKey(Users, db_index=True , on_delete=models.SET_NULL, null=True)
        createdAt = models.DateTimeField(auto_now_add=True)
        updatedAt = models.DateTimeField(auto_now=True)
        
        def __str__(self):
           return f"{self.name} ({self.checkInTime} - {self.checkOutTime})"


def isRole(value):
    if value in ["LEADER" , "CO-LEADER","MEMBER"]:
        return value
    else:
        raise ValidationError("invalid employee role")


class TeamMember(models.Model):
        role = models.CharField(
             max_length=10 ,
             db_index=True,
             validators=[
                  isRole
             ]
        )
        TeamId =models.ForeignKey(Team, db_index=True , on_delete=models.CASCADE, null=True)
        OrganizationId =models.ForeignKey(Organization, db_index=True , on_delete=models.CASCADE, null=True)
        userId = models.ForeignKey(Users , db_index=True , on_delete=models.CASCADE, null=True)
        # addedBy = models.ForeignKey(Users, db_index=True , on_delete=models.SET_NULL, null=True)
        createAt = models.DateTimeField(auto_now_add=True)
        updatedAt = models.DateTimeField(auto_now=True)

        def __str__(self):
           return f"{self.role} | {self.OrganizationId.name} | ({self.userId.firstName} {self.userId.lastName})"
        
# tm.objects.filter(OrganizationId = o , TeamId_id__in = teamDetails) 
#>>> teamMem = t.objects.annotate(count = Count('teammember'))                          