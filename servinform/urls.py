from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('bases.urls','bases'), namespace='bases')),
    path('bd/', include(('bd.urls', 'bd'), namespace='bd')),
    path('import/', include(('export.urls', 'export'), namespace='export')),


    path('admin/', admin.site.urls),
]
