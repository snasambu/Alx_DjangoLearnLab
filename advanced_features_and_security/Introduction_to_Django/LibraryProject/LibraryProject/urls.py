from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('relationship_app.urls')),  # Home page and other views
    path('relationship_app/', include('relationship_app.urls')),

]
