from django.urls import path
from . import views

urlpatterns = [
    path("project", views.project, name="project"),
    path("test1", views.test1, name="test1"),
    path(
        "getExchangeOrderDetailsData",
        views.getExchangeOrderDetailsData,
        name="getExchangeOrderDetailsData",
    ),
    path(
        "getPurchaseordersData",
        views.getPurchaseordersData,
        name="getPurchaseordersData",
    ),
    path("getSalesVolumeData", views.getSalesVolumeData, name="getSalesVolumeData"),
    path("getSalesQuantity", views.getSalesQuantity, name="getSalesQuantity"),
    path(
        "getSalesVolumeBySalesperson",
        views.getSalesVolumeBySalesperson,
        name="getSalesVolumeBySalesperson",
    ),
    path(
        "getSumSalesVolumeData",
        views.getSumSalesVolumeData,
        name="getSumSalesVolumeData",
    ),
]
