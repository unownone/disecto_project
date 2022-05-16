import random
import string
from django.db import models

from user.models import User


def generate_random_id():
    text_part = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    num_part = "".join(random.choice(string.digits) for _ in range(5))
    return text_part + "-" + num_part


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="item_images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "items"

    def __str__(self):
        return str(self.name)


class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    invoice_id = models.CharField(
        default=generate_random_id, max_length=8, null=True, blank=True
    )
    is_placed = models.BooleanField(default=False)

    class Meta:
        db_table = "purchases"

    def __str__(self):
        return str(self.id)


class Purchased_item(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    class Meta:
        db_table = "purchased_items"

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):

        if self.count == 0:
            return self.delete()
        self.price = self.item.price * self.count
        return super().save(*args, **kwargs)
