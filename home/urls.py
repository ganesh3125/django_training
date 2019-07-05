from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home_view,name='home'),
    #or path('',views.home_view),
    path('deletestudent/<id>',deletestudent),
    path('editstudent/<id>',editstudent),
    path('createstudent/',createstudent),
    path('contact/',contact_view),
    path('about/',about_view),
    path('admin/', admin.site.urls),
]