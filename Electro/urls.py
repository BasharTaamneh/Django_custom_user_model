from django.urls import path
from .views import (
    ElectroHomeView,
    ElectroListView,
    ElectroDetailView,
    ElectroCreateView,
    ElectroUpdateView,
    ElectroDeleteView,
    AboutPageView,
)


urlpatterns = [
    path("", ElectroHomeView.as_view(), name="home"),
    path("electro/", ElectroListView.as_view(), name="electro_list"),
    path("electro/<int:pk>/", ElectroDetailView.as_view(), name="electro_detail"),
    path("electro/create/", ElectroCreateView.as_view(), name="electro_create"),
    path(
        "electro/<int:pk>/update/", ElectroUpdateView.as_view(), name="electro_update"
    ),
    path(
        "electro/<int:pk>/delete/", ElectroDeleteView.as_view(), name="electro_delete"
    ),
    path('about/', AboutPageView.as_view(), name='about'),
]
