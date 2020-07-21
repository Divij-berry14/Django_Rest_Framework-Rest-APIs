from django.urls import path
from Form import views
#DataFlair #Url-ConfigWhen we validate our form data, we are actually c

urlpatterns = [
    path('', views.regform, name = 'registration form'),
    path("createProduct/",views.ProductCreateView,name="CreateProduct"),
    # path("res/",views.res,name="res")
]