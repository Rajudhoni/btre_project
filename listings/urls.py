from django.urls import path
from listings import views


urlpatterns = [
    path('', views.index,name='listings'),
    path('<int:listingg_id>',views.listingg,name ='listingg'),
    path('search',views.search,name ='search'),
]
