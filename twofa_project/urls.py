from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # For login/logout views
    path('', include('twofa_app.urls')),  # Our app's URLs
]
