from django.urls import re_path as url
from runcard.views import barcodepage

urlpatterns = [
    url(r'', barcodepage, name='barcodepage'),
]