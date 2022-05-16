from django.urls import path
from sell_app.views import (
    PurchaseCreateView,
    PurchaseDetailView,
    ItemListApiView,
    PurchasedItemView,
)

urlpatterns = (
    path("items/", ItemListApiView.as_view()),
    path("purchase/", PurchaseCreateView.as_view()),
    path("add-items/<pk>/", PurchasedItemView.as_view()),
    path("purchase/<pk>/", PurchaseDetailView.as_view()),
)
