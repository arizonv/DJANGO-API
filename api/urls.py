from django.urls import path
from .views import LoginAPIView,UserLogout,UserList,Register,UserReport

app_name = 'api'

urlpatterns = [
    # AUTH  ######################################################
    path('auth/', LoginAPIView.as_view(), name='login'),
    path('out/', UserLogout.as_view(), name='logout'),
    # USERS ######################################################
    # SERVICES ###################################################
    # RESPORT ####################################################


]

