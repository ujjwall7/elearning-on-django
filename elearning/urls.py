from django import views
from django.urls import path
from .import views


urlpatterns = [
    path('',views.index,name="index"),
    path('#contactus_section',views.contactUs,name="contactus"),
    path('#GiveFeedback',views.givefeedback,name="givefeedback"),    
    path('#ournewsletter',views.ournewsletter,name="ournewsletter"),    
    path('register',views.register,name="register"),
    path('UserRegister',views.Register,name="UserRegister"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('LoginUser/',views.LoginUser,name="LoginUser"),
    path('quiz/',views.quiz,name="quiz"),
    path('jee/',views.jee,name="jee"),
    path('gate/',views.gate,name="gate"),
    path('courses/',views.courses,name="courses"),
    path('profile/',views.profile,name="profile"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('downloadnotes/',views.downloadnotes,name="downloadnotes"),
]