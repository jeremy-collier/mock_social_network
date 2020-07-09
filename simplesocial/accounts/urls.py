from django.conf.urls import url
#This allows us to automatically have a login/logout view but since
#it's just views, we import it as auth_views so we can distinguish
from django.contrib.auth import views as auth_views

from . import views

#Allows you to use url templates to reference app
app_name = 'accounts'

urlpatterns = [
    url(r'^login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    url(r'^logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),

]
