from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.


class Variety(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250)
    latin = models.CharField(max_length=250, blank=True, null=True)
    category = TreeForeignKey('Category')
    is_stock = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "varieties"


class Category(MPTTModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=250, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    level = models.PositiveIntegerField(default=0)
    lft = models.PositiveIntegerField(default=0)
    rght = models.PositiveIntegerField(default=0)
    tree_id = models.PositiveIntegerField(default=0)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"

    class MPTTMeta:
        order_insertion_by = ['title']