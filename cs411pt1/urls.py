"""
URL configuration for cs411pt1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from myapp import views
from myapp.views import paper_statistics
from myapp.views import LoginView, DataUserView, InteractiveDataUserView
from django.contrib import admin

urlpatterns = [
    path('api/data/interactive/user/<int:user_id>/', InteractiveDataUserView.as_view(), name='interactive-data-user'),
    path('api/data/user/<int:user_id>/', DataUserView.as_view(), name='data-user'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('', views.paper_statistics, name='article-data'),
    path('api/post_data/', views.post_data, name='post-data')
]
