"""crudop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
""
from django.contrib import admin
from django.urls import path
#from apps import views
from apps.views import *





urlpatterns = [
    path('admin/', admin.site.urls),
    path('',show,name="show"),
    path('renderpdf/',renderpdf,name="renderpdf"),
    path('editview',editview,name='editview'),
    path('ajax_posting/',ajax_posting,name="ajax_posting"),
    path('get_data/', get_data, name='get_data'),
    # path('editview/', Editview, name='editview'),
    # path('updateview/', get_data, name='updateview'),
    path('deleteview/', deleteview, name='deleteview'),
    path('Priti_Excel/', Karan_Excel_Report, name='Karan_Excel_Report'),

]




