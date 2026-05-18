from django.urls import include, re_path
import MyApp1.views 
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views


"""


Project_Practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app1 import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    re_path(r'^$', MyApp1.views.home, name='home'),
    re_path(r'^home$', MyApp1.views.index, name='index'),
    path(r'input', MyApp1.views.input_view, name='input'),
    re_path(r'assign', MyApp1.views.assign_view, name='assign'),
    #path("",MyApp1.views.home, name="home"),
    path("teachers/", MyApp1.views.login, name="teacher"),
    path('report/', MyApp1.views.report, name='report'),
    path('signup/', MyApp1.views.signup_view, name='signup'),
     # Uses Django's built-in login logic
    path('login/', auth_views.LoginView.as_view(template_name='MyApp1/login.html'), name='login'),
    path('home2/', MyApp1.views.home2,name='home2'),
    path('unit_course/', MyApp1.views.unit_course, name='unit_course'),

]
    
admin.site.site_header = "BSSS administration"

admin.site.index_title = "Welcome to BSSS"
admin.site.site_title = "Bsss Admin"