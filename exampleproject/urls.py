from django.urls import path
from . import views
urlpatterns = [
    path('',views.projects,name="projectslink"),
    path('project/<str:cookie>/',views.project,name="projectlink"),
    path('create-project/',views.createProject,name="create-project"),
    path('update-project/<str:pk>',views.updateProject,name='updateproject'),
    path('delete-project/<str:pk>',views.deleteproject,name = 'delproject'),
    path('create-semester/',views.createSemester,name="create-semester"),
    path('create-branch/',views.createBranch,name="create-branch"),
    path('create-subject/',views.createSubject,name="create-subject"),
    path('create-unit/',views.createUnit,name="create-unit"),
    path('create-topic/',views.createTopic,name="create-topic"),
    path('semester/<str:pk>/',views.semestersh,name="semestersh"),
    path('branch/<str:cookie>/',views.branchesh,name="branchi"),
    path('subject/<str:pk>/',views.subjectsh,name="subjecti"),
    path('unit/<str:cookie>/',views.unitish,name="uniti"),
    path('create-timetable/',views.createTT,name="create-TT"),
    path('customise/',views.custom_hrs,name="custom_hrs"),
    path('demo/',views.demo,name="demo"),
    path('select-subjects/',views.selectsubjects,name="select-subjects"),
    path('select-units/',views.selectunits,name="select-units"),
    path('subjecthrs/',views.subjecthours,name="subjecthrs"),
    path('schedule/<str:pk>/',views.schedule,name="schedule"),
    #path('subject-hrs/',views.subjecthours,name="subjecthrs"),
 
    
    
]
