from email import message
from django.shortcuts import redirect, render

from .models import *


def index(request):
    if(isLoggedIn(request)!=True):
        return redirect("login")
    else:
        return render(request,'elearning/index.html')


def register(request):
    return render(request,'elearning/register.html')


def Register(request):
    if request.method == "POST":
        fname=request.POST['fname']
        Email=request.POST['email']
        profile=request.FILES['file']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        
        # First we will validate that user already exist
        User=UserRegister.objects.filter(EMAIL_ADDRESS=Email)

        if User:
            message="User Already Exist"
            return render(request,"elearning/register.html",{'msg':message})

        else:
            if password == cpassword:
                NewUser=UserRegister.objects.create(FULLNAME=fname,
                                                    EMAIL_ADDRESS=Email,
                                                    PASSWORD=password,
                                                    Profile=profile)
                message="User Sucessfully Registerd"
                return render(request,"elearning/login.html",{'msg':message})
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request,"elearning/register.html",{'msg':message})

def login(request):
    return render(request,'elearning/login.html')


def contactUs(request):
    if request.method=="POST":
        firstName=request.POST['fname']
        lastName=request.POST['lname']
        email=request.POST['email']
        message=request.POST['message']
        additionalDetail=request.POST['addtional']

        contact=ContactUs.objects.create(FirstName=firstName,
                                         LastName=lastName,
                                         Email=email,
                                         Message=message,
                                         AdditionalDetails=additionalDetail)

        message="Message Send Sucessfully"
        return render(request,"elearning/index.html",{'msg':message})




def givefeedback(request):
    if request.method=="POST":
        yourname=request.POST['yname']
        email=request.POST['email']
        additionalDetail=request.POST['addtional']

        contact=GiveFeedback.objects.create(YourName=yourname,
                                         Email=email,
                                         AdditionalDetails=additionalDetail)

        message="Message Send Sucessfully"
        return render(request,"elearning/index.html",{'msgg':message})




def ournewsletter(request):
    if request.method=="POST":
        Email=request.POST['email']

        contact=OurNewsletter.objects.create(EnterYourEmail=Email)

        message="Message Send Sucessfully"
        return render(request,"elearning/index.html",{'msgo':message})



def LoginUser(request):
    if request.method=="POST":
        Email=request.POST['email']
        Password=request.POST['password']

        # Checking the emailid with database
        user=UserRegister.objects.get(EMAIL_ADDRESS=Email)

        if user:
            if user.PASSWORD == Password:
                
                #session start
                request.session['saved_email']=Email
                request.session['saved_password']=Password

                return redirect('index')
            
            else:
                message="Password does not match"
                return render(request,"elearning/login.html",{'msg':message})
        else:
            message="User does not exist"
            return render(request,"elearning/register.html",{'msg':message})
 

def isLoggedIn(request):
    if request.session.has_key('saved_email'):
        return True
    else:
        return False


def logout(request):
    del request.session['saved_email']
    return redirect("login")


def quiz(request):
    if(isLoggedIn(request)!=True):
        return redirect("login")
    else:
        return render(request,'elearning/quiz.html')


def jee(request):
    if(isLoggedIn(request)!=True):
        return redirect("login")
    else:
        return render(request,'elearning/jee.html')
    
    
def gate(request):
    if(isLoggedIn(request)!=True):
        return redirect("login")
    else:
        return render(request,'elearning/gate.html')


def courses(request):
    if(isLoggedIn(request)!=True):
        return redirect("login")
    else:
        return render(request,'elearning/computer_courses.html')


def profile(request):
    if request.session.has_key('saved_email'):
        user_email=request.session['saved_email']
        myUser=UserRegister.objects.get(EMAIL_ADDRESS=user_email)
        return render(template_name="elearning/profile.html",
        request=request,context={"profile":myUser})
    else:
        return redirect("/")



def delete(request,id):
    ddata=UserRegister.objects.get(id=id)
    ddata.delete()
    return redirect('register')


def downloadnotes(request):
    if request.session.has_key('saved_email'):
     
        dnotes = None

        categories = Category.get_all_categories() 


        categoryID = request.GET.get('category') 
        if categoryID: 
            dnotes = Dnotes.get_all_Dnotes_by_id(categoryID) 
        else :
            dnotes = Dnotes.get_all_Dnotes();


        data = {} 
        data['dnotes'] = dnotes 
        data['categories'] = categories

        return render(request,'elearning/downloadnotes.html',data)
    
    else:
        return redirect('login')


















