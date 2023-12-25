"""proj1 URL Configuration

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
from django.contrib import admin
from django.urls import include, path   # incluce の import を追加

urlpatterns = [
    path('admin/', admin.site.urls),    # 最初からある記述
    path('chapter02/', include('chapter02.urls')),  # 追加
    path('chapter03/', include('chapter03.urls')),  # 追加
    path('chapter04/', include('chapter04.urls')),  # 追加
    path('chapter05/', include('chapter05.urls')),  # 追加
    path('chapter06/', include('chapter06.urls')),  # 追加
    path('chapter07/', include('chapter07.urls')),  # 追加
    path('chapter08/', include('chapter08.urls')),  # 追加
    path('chapter09/', include('chapter09.urls')),  # 追加
    path('chapter10/', include('chapter10.urls')),  # 追加
    path('bs/', include('bs_sample.urls')),  # 追加
]


