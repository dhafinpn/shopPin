from django.urls import path
from main.views import show_main, create_review_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from django.urls import path, include
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_review, delete_review

app_name = 'main'

urlpatterns = [
    path('login/', login_user, name='login'),
    path('', show_main, name='show_main'),
    path('create_review_entry',create_review_entry, name='create_review_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('edit-review/<uuid:id>', edit_review, name='edit_review'),
    path('delete/<uuid:id>', delete_review, name='delete_review'),
]