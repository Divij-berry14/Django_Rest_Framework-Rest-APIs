from django.urls import path,include
from snippets import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('snippets/',views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # path('snippetsDetail/', views.SnippetDetail.as_view())
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/',obtain_auth_token,name='obtain-token')
]