from rest_framework import viewsets, mixins
from rest_framework.authentication import  TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from db.models import Offer, Reward
from api.serializers import OfferSerializer, RewardSerializer
from django.shortcuts import get_object_or_404

# OfferViewSet to manage, and perform retrieve operation on coupons_offer
class OfferViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    # Token Authentication for the whole view
    authentication_classes=[TokenAuthentication]

    # No unauthenticated user can view or make coupons
    permission_classes = [IsAuthenticated]

    queryset = Offer.objects.all()

    serializer_class = OfferSerializer

    # Search for coupons matching the code
    lookup_field = 'code'

# RewardViewSet to manage, and perform retrieve operation on coupons_rewards
class RewardViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    # Token Authentication for the whole view
    authentication_classes=[TokenAuthentication]

    # No unauthenticated user can view or make coupons
    permission_classes = [IsAuthenticated]

    queryset = Reward.objects.all()

    serializer_class = RewardSerializer

    # Search for coupons matching the code
    lookup_field = 'code'
