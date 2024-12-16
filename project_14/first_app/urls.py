

from django.urls import path,include
from .import views
urlpatterns = [
    
    path('',views.home,name='homepage'),
    path('model/',views.model,name='modelpage')
]