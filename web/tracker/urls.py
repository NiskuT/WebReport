from django.urls import path
from . import views

urlpatterns = [

    # --- Pages ---

    path("", views.index, name="index"),
    path("signin", views.signin_view, name="signin"),
    path("signout", views.signout_view, name="signout"),
    path("add", views.add_view, name="add")
]

"""     path("periods", views.periods_view, name="periods_view"),

    path("project/<str:key>", views.project_view, name="project"),   # PPPP
    path("group/<str:key>", views.group_view, name="group"),         # PPPP-GG
    path("task/<str:key>", views.task_view, name="task"),             # PPPP-GG-TTTT


    # --- API Routes ---

    path("api/periods/<str:tag>", views.samples, name="periods"),    # all, open, closed

    # make it unique? for the views several...
    path("api/project/<str:key>", views.project, name="project"),   # PPPP
    path("api/group/<str:key>", views.group, name="group"),         # PPPP-GG
    path("api/task/<str:key>", views.task, name="task")             # PPPP-GG-TTTT
 """