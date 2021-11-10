"""qrkiosk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from django.conf.urls.static import static
from django.conf import settings
from board_app.views import BoardView, PostView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kiosk.urls')),
    path('board/', BoardView.as_view(), name='board'),
    path('post/', PostView.as_view(), name='post'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)