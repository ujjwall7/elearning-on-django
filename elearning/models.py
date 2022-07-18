from asyncio.windows_events import NULL
from email.policy import default
from sqlite3 import connect
from tkinter.tix import IMAGE
from unicodedata import category
from django.db import models
from django.forms import CharField

class UserRegister(models.Model):
    FULLNAME=models.CharField(max_length=50)
    EMAIL_ADDRESS=models.EmailField(max_length=254)
    PASSWORD=models.CharField(max_length=50)
    Profile=models.ImageField(upload_to="profile", default='')

    def __str__(self):
        return self.FULLNAME




class ContactUs(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    Email=models.EmailField(max_length=254)
    Message=models.CharField(max_length=50)
    AdditionalDetails=models.CharField(max_length=50)

    def __str__(self):
        return self.FirstName



class GiveFeedback(models.Model):
    YourName=models.CharField(max_length=350)
    Email=models.EmailField(max_length=254)
    AdditionalDetails=models.CharField(max_length=350)

    def __str__(self):
        return self.YourName




class OurNewsletter(models.Model):
    EnterYourEmail=models.EmailField(max_length=254)

    def __str__(self):
        return self.EnterYourEmail



class Category(models.Model):
    Categoryname=models.CharField(max_length=200)

    @staticmethod 
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.Categoryname

    



class Dnotes(models.Model):
    Name=models.CharField(max_length=250)
    File=models.FileField(upload_to="notes")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.Name


    @staticmethod 
    def get_all_Dnotes():
        return Dnotes.objects.all()


    @staticmethod 
    def get_all_Dnotes_by_id(category_id):
        if category_id : 
            return Dnotes.objects.filter(category=category_id) 
        else :
            return Dnotes.get_all_Dnotes();



    


