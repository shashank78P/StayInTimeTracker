from django.urls import path
from . import views

urlpatterns = [
    # path("get-user-by-email" , views.getUserByEmail),
    path("sign-up" , views.signUp),
    
    path("sign-up-2" , views.signUp2),
    path("log-in" , views.login , name="users-log-in"),
    path("log-out" , views.logout),
    path("change-password" , views.ChangePassword),
    path("change-password-pre" , views.ChangePassword1),
    path("add" , views.add),
    path("edit/<slug:slug>" , views.edit ),
    path("set-current-active-organization" , views.setCurrentActiveOrganization),
    path("attendance-history/<slug:slug>" , views.attendanceHistory),
    path("attendance-history/<slug:slug>/<str:takenAt>" , views.getAttendanceInDetailsByDay),
    path("" , views.homePage),
    path("<slug:slug>" , views.home),
    path("<slug:slug>/edit" , views.editUserData),

    path("leave-request/<slug:slug>" , views.leaveRequest),
    path("leave-request/<slug:slug>/add" , views.addLeaveRequest),
    path("leave-request/<slug:slug>/<id>" , views.seeLeaveRequest),
    path("leave-request/<slug:slug>/delete/<id>" , views.deleteLeaveRequest),
    
    # insights
    # /2023-12-01T13:52:08.156Z/2023-12-31T13:52:08.156Z
    path("leave-type/<slug:slug>/get-leave-type-insight-of-user/<str:fromDate>/<str:toDate>" , views.getLeaveTypeInsightOfUser),
    path("attendance/<slug:slug>/get-attendance-by-team-org/<str:fromDate>/<str:toDate>" , views.getAttendanceByTeamOrg),

]