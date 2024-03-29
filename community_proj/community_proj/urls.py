"""community_proj URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from community_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', new, name="new"),
    path('detail/<int:community_id>/', detail, name="detail"),
    path('', index, name="index"),
    path('comment/<int:community_id>/', comment, name="comment"),
    path('account/', include('account.urls')),
    path('update/<int:community_id>/', update, name="update"),
    path('delete/<int:community_id>/', delete, name="delete"),
    path('comment_delte/<int:comment_id>/', comment_delete, name="comment_delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

handler404 = 'community_app.views.page_not_found'