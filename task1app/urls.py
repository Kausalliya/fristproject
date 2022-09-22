from . import views
from django.urls import path

urlpatterns = [
    path('open_main',views.open_main,name='open_main'),
    path('open_thekkady',views.open_thekkady,name='open_thekkady'),
    path('open_wayanad',views.open_wayanad,name='open_wayanad'),
    path('open_vagamon',views.open_vagamon,name='open_vagamon'),
    path('open_alleppey',views.open_alleppey,name='open_alleppey'),

    path('open_sample',views.open_sample,name='open_sample'),
    path('open_add',views.open_add,name='open_add'),
    path('add_num',views.add_num,name='add_num')
  
]
