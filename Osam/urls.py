from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from contents import views as cont_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',cont_views.index,name='index'),
    path('about/',cont_views.about,name='about'),
    path('contact/',cont_views.contact,name='contact'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    