from django.urls import path
from carAPI.views import CarViewAPI,CarDetailAPI, CarViewAPIMixin, CarDetailAPIMixin

urlpatterns = [
    path('', CarViewAPI.as_view()),
    path('<int:pk>', CarDetailAPI.as_view()),
    path('carMixin/', CarViewAPIMixin.as_view()),
    path('carMixin/<int:pk>', CarDetailAPIMixin.as_view()),
    
    #mixins urls
    
]
