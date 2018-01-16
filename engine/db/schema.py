import graphene

from graphene_django.types import DjangoObjectType

from db.models.inventory import Inventory, Site

class SiteType(DjangoObjectType):
    class Meta:
        model = Site

class InventoryType(DjangoObjectType):
    class Meta:
        model=Inventory

class Query(object):
    all_sites = graphene.List(SiteType)
    all_inventories = graphene.List(InventoryType)

    def resolve_all_sites(self, info, **kwargs):
        return Site.objects.all()

    def resolve_all_inventories(self, info, **kwargs):
        return Inventory.objects.select_related('site').all()
