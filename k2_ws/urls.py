from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


urlpatterns = [
    url(r'^$', view=admin.site.login, name='admin'),  # Admin je početna stranica!
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('hvk.urls')),
    url(r'^sim/', include('sim.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^obtain-token/', obtain_jwt_token),
    url(r'^verify-token/', verify_jwt_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
