from django.urls import path
from core.views import *

urlpatterns = [
    path('',home, name='index'),
    path('about-me/',about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', contact,name='contact')

]