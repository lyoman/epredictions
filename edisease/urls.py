"""edisease URL Configuration

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
from django.urls import include , path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = "E-Disease Prediction"
admin.site.index_title = 'E-Disease Prediction Site Administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^', admin.site.urls),
    # path('/', admin.site.urls),
    path('api/auth/token/', obtain_jwt_token),
    path('api/users/', include(("accounts.api.urls",'accounts-api'), namespace='accounts-api')),
    path('api/prediction/', include(("prediction.api.urls",'prediction-api'), namespace='prediction-api')),
    path('api/drugsearch/', include(("drugsearch.api.urls",'drugsearch-api'), namespace='drugsearch-api')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
