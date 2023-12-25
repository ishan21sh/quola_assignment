from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('scan_id/',views.scan_id),
    path('scan_id/submit_id/<str:image_id>',views.submit_id),
    path('id_card/<str:pk>',views.display_id),
    path('update_card/<str:pk>',views.update_id),
    path('delete_card/<str:pk>',views.delete_id)
]