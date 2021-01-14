from django.urls import path, include
from snippets import views
from snippets.views import *
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    # path('snippets/',views.SnippetList.as_view()),
    # path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    # # path('snippetsDetail/', views.SnippetDetail.as_view())
    # path('api-auth/', include('rest_framework.urls')),
    # path('api/token/',obtain_auth_token,name='obtain-token'),
    # path('login/',views.LoginView.as_view()),
    # path('logout/',views.LogoutView.as_view()),
    # path("res/",views.res,name="res")
    path('poll/', views.poll),
    path('poll/<int:id>/', views.poll_details),
    path('pollAPI/', PollAPIView.as_view()),
    path('pollAPI/<int:id>/', Poll_detailsAPI.as_view()),
    path('title/', get_title.as_view()),
    path('generics/poll/', PollListView.as_view())
]