from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PresentSerializer
from .models import *


@require_http_methods(["GET"])
def isPartisipant(request):
    # /IsPartisipant/?tg_id={}
    # GET only
    tg_id = request.GET.get('tg_id')
    partisipant=Partisipant.objects.filter(
        tg_id=tg_id
        ).exists()

    if not partisipant:
        partisipant=Partisipant.objects.create(
            tg_id=tg_id
            )
        status=201

    else:
        status=200

    return HttpResponse(status=status)

@require_http_methods(['GET'])
def Pay(request):
    # /Pay/?tg_id={}&amount={}
    tg_id = request.GET.get('tg_id')
    amount = request.GET.get('amount')
    
    partisipant = Partisipant.objects.get(
        tg_id=tg_id
        )

    pay = PartisipantPay.objects.create(
        account= partisipant,
        amount = amount
        )
    return HttpResponse(status=200)


@require_http_methods(["GET"])
def getCategories(request):
    tg_id = request.GET.get('tg_id')
    partisipant=Partisipant.objects.get(
        tg_id=tg_id
        )
    return HttpResponse(
        partisipant.get_available_categories(),
        status=200,
        content_type='application/json'
        )
    
class getPresentsList(APIView):
    def get(self, request):
        tg_id = request.query_params.get('tg_id')
        
        presents=PartisipantPresent.objects.filter(
            owner__tg_id = tg_id
            )
        serializer=PresentSerializer(
            presents,
            many=True
            )

        return Response(serializer.data)


class getPresent(APIView):
    def get(self, request):
        # getPresent/?tg_id={}&category={}
        # GET only
        tg_id = request.GET.get('tg_id')
        category = int(request.GET.get('category'))
    
        owner = Partisipant.objects.get(tg_id = tg_id)

        present=PartisipantPresent.objects.create(
            owner = owner,
            category = category
            )
    
        serializer = PresentSerializer(present)

        return Response(serializer.data)

