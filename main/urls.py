from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import increase, decrease, remove_all, profile, get_item_json, create_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('increase/<int:id>/', increase, name='increase'),
    path('decrease/<int:id>/', decrease, name='decrease'),
    path('remove_all/<int:id>/', remove_all, name='remove_all'),
    path('profile/', profile, name="profile"),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', create_ajax, name='create_ajax')
]