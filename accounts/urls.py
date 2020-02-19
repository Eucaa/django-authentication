#  This file will keep all of the accounts specific code inside of the accounts app(folder) which means all of the created URLs (apart from 'index') can go inside this file.
from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name='logout'),  # Refers to "{% url 'logout' %}" in the base.html template.
    url(r'^login/$', login, name='login'),  # Refers to "{% url 'login' %}" in the base.html template.
    url(r'^register/$', registration, name='registration'),  # Refers to "{% url 'registration' %}" in the base.html template.
    url(r'^profile/$', user_profile, name='profile'),   # Refers to "{% url 'profile' %}" in the base.html template.
    url(r'^password-reset/', include(url_reset))  # With this, all of the urlpatterns in the url_reset.py file, will be connected to this url.
]
