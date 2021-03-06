"""todoro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from files.models import FileViewSet
from tasks.api import TaskViewSet
from tasks.views import tasks_list, tasks_detail, NewTaskView
from users.api import UserViewSet
from users.views import LoginView, logout

router = DefaultRouter()
router.register("users", UserViewSet, base_name="users_api")
router.register("tasks", TaskViewSet)
router.register("files", FileViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', tasks_list, name="tasks_list"),  # si la URL es /, ejecutar función tasks_list
    url(r'^tasks/(?P<task_pk>[0-9]+)$', tasks_detail, name="tasks_detail"),
    url(r'^tasks/new$', NewTaskView.as_view(), name="tasks_new"),
    url(r'^login$', LoginView.as_view(), name="login"),
    url(r'^logout$', logout, name="logout"),

    # API Users & Tasks
    url(r'^api/1.0/', include(router.urls))
]
