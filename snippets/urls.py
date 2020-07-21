from django.urls import path,include
from snippets import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('snippetsDetail/', views.SnippetDetail.as_view())
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/',obtain_auth_token,name='obtain-token'),
    path('login/',views.LoginView.as_view()),
    path('logout/',views.LogoutView.as_view()),
    path("res/",views.res,name="res")
]