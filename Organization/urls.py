from django.urls import path
from . import views

urlpatterns = [
    path("create-organization" , views.createOrganization),
    path("get-all-organization-list" , views.getAllOrganizationList),
    path("leave-request/<slug:slug>" , views.leaveRequest),

    path("teams/<slug:slug>" , views.teams),
    path("teams/<slug:slug>/create-team" , views.createTeam),
    path("teams/<slug:slug>/<id>" , views.teamMembersDetails),
    path("teams/<slug:slug>/add/<teamId>" , views.addTeamMember),
    path("teams/<slug:slug>/edit/<teamId>" , views.editTeam),
    path("teams/<slug:slug>/delete/<teamId>" , views.delteTeam),
    path("teams/<slug:slug>/edit/<teamId>/<id>/<employeeId>" , views.editTeamMember),
    path("teams/<slug:slug>/delete/<teamId>/<id>/<employeeId>" , views.deleteTeamMember),
    
    path("job-title/<slug:slug>" , views.jobTitle),
    path("job-title/<slug:slug>/add" , views.AddJobTitle),
    path("job-title/<slug:slug>/edit/<id>" , views.EditJobTitle),
    path("job-title/<slug:slug>/delete/<id>" , views.DeleteJobTitle),

    path("job-title/<slug:slug>/<jobTitleId>" , views.jobTitleDetails),
    path("job-title/<slug:slug>/edit/<jobTitleId>/<employeeId>" , views.editEmployee),
    path("job-title/<slug:slug>/add/<jobTitleId>" , views.addEmployeeViaJobDetails),
    path("job-title/<slug:slug>/delete/<jobTitleId>/<employeeId>" , views.deleteEmployee),

    path("employees/<slug:slug>" , views.employees),
    path("employees/<slug:slug>/add" , views.AddEmployee),
    path("<slug:slug>" , views.companyProfile),
]
    # path("add-job-title" , views.AddJobTitle),
    # path("job-title/<slug:slug>/<id>" , views.jobTitleDetails),