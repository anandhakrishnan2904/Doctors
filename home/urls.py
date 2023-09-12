from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from . import views
from django.conf.urls.static import static
urlpatterns = [
   
    path('',views.index, name='home' ),
    path('about/',views.about,name='about' ),
    path('booking',views.booking,name='booking' ),
    path('doctors',views.doctor,name='doctors' ),
    path('contact',views.contact,name='contact'),
    path('department',views.department,name='department'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


