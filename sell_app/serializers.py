from rest_framework import serializers
from sell_app.models import Item, Purchase, Purchased_item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchasedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchased_item
        fields = "__all__"
