from django.contrib import admin
from elearning .models import *
# Register your models here.


class registerdisplay(admin.ModelAdmin):
    list_display=['FULLNAME','EMAIL_ADDRESS','PASSWORD','Profile']

admin.site.register(UserRegister,registerdisplay)


class ContactUsdisplay(admin.ModelAdmin):
    list_display=['FirstName','LastName','Email','Message','AdditionalDetails']

admin.site.register(ContactUs,ContactUsdisplay)


class GiveFeedbackdisplay(admin.ModelAdmin):
    list_display=['YourName','Email','AdditionalDetails']

admin.site.register(GiveFeedback,GiveFeedbackdisplay)



admin.site.register(OurNewsletter)



class Dnotesdisplay(admin.ModelAdmin):
    list_display=['Name','File','category']

admin.site.register(Dnotes,Dnotesdisplay)



admin.site.register(Category)
