from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gemini/', include('gemini.urls')),
    path('', RedirectView.as_view(url='gemini/', permanent=False)),  # Redirect root to gemini/
]