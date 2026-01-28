from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('patient/', include('patient.urls')),
    path('auth/', include('myauthapp.urls')),
    path('user/', include('user.urls')),
    path('upload/', include('fileupload.urls')),
    path('project/', include('projectsubmission.urls')),
    path('notes/', include('notes.urls')),
    path('registration/', include('registration.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
