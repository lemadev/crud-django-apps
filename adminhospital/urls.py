from django.urls import path
from . import views

urlpatterns = [
    path("", views.adminh_index, name="admin_index"),
    path("<int:id>/", views.detail_turn, name="detail_turn"),
    path("<int:id>/", views.delete_turn, name="turn_detail"),
    path("/", views.new_turn, name="new_turn"),
    path("<int:id>", views.delete_turn, name="delete_turn"),

    path("medic/indexMedics/", views.indexMedics, name="indexMedics"),
    path("medic/edit_medic/<int:id>", views.edit_medic, name="edit_medic"),
    path("medic/delete_medic/<int:id>", views.delete_medic, name="delete_medic"),
    path("medic/new_medic/", views.new_medic, name="new_medic"),

    path("turn/indexPersons/", views.indexPersons, name="indexPersons"),
    path("turn/edit_person/<int:id>", views.edit_person, name="edit_person"),
    path("turn/delete_person/<int:id>", views.delete_person, name="delete_person"),
    path("turn/new_person/", views.new_person, name="new_person"),
]