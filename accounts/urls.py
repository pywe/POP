from django.conf.urls import url,include
from . import views


urlpatterns = [
    url(r"^$",views.index, name="home"),
    url(r"^campaigns/new-session/$",views.new_session, name="new-session"),
    url(r"^accounts/login/$",views.login_view, name="login"),
    url(r"^api/v1/auth/$",views.api_login, name="api-login"),
    url(r"^api/v1/campaigns/fetch/$",views.fetch_campaigns, name="fetch-campaigns"),
]