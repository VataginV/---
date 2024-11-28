"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from tos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.gl, name='home'),
    path('Документы', views.doc, name='doc'),
    path('О Тосах', views.tos, name='tos'),
    path('Авторизация', views.auth, name='auth'),
    path('Конкурсы', views.comp, name='comp'),
    path('Новости', views.news, name='news'),
    path('Новости/<int:id>/', views.news_detail, name='news_detail'),
    path('Регистрация', views.registration, name='registration'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
