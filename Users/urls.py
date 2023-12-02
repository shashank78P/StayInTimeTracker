from django.urls import path
from . import views

urlpatterns = [
    # path("get-user-by-email" , views.getUserByEmail),
    path("sign-up" , views.signUp),
    path("log-in" , views.login),
    path("add" , views.add),
    path("edit/<slug:slug>" , views.edit ),
    path("set-current-active-organization" , views.setCurrentActiveOrganization),
    path("attendance-history/<slug:slug>" , views.attendanceHistory),
    path("" , views.homePage),
    path("<slug:slug>" , views.home),
    path("profile/<slug:slug>" , views.index , name="user-profile"),
]