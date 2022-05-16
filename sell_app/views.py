from re import S
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from sell_app.models import Item, Purchase, Purchased_item
from sell_app.serializers import (
    ItemSerializer,
    PurchaseSerializer,
    PurchasedItemSerializer,
)
from sell_app.utils import render_pdf, sanityData
from django.db.models import Sum

# Create your views here.


class ItemListApiView(generics.ListAPIView):
    serializer_class = ItemSerializer
    queryset = Item.objects.all().order_by("-created_at")


class PurchaseCreateView(generics.ListCreateAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        q = Purchase.objects.filter(user=self.request.user).order_by("-created_at")
        return q

    def post(self, request, *args, **kwargs):
        data = sanityData(request.data)
        data["user"] = request.user.id
        request.data.update(data)
        return super().post(request, *args, **kwargs)


class PurchaseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        obj = Purchase.objects.filter(pk=pk, user=self.request.user)
        if obj.exists():
            return obj.prefetch_related("purchased_item_set").first()
        else:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        final = render_pdf(
            "purchase_detail.html",
            {
                "purchases": obj,
                "final": obj.purchased_item_set.aggregate(Sum("price")),
            },
        )
        resp = HttpResponse(final, content_type="application/pdf")
        resp["Content-Disposition"] = "inline; filename=purchase_detail.pdf"
        return resp


class PurchasedItemView(generics.CreateAPIView):
    serializer_class = PurchasedItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def get_object(self):
    #     obj = Purchase.objects.filter(pk=self.request.data.pop("id"), is_placed=False)
    #     if obj.exists():
    #         return obj.first()
    #     else:
    #         raise Http404

    def post(self, request, pk, *args, **kwargs):
        print()
        data = sanityData(request.data)
        data["user"] = request.user.id
        data["purchase"] = pk
        request.data.update(data)
        return super().post(request, *args, **kwargs)
