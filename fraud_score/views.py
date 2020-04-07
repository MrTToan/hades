from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from pipeline import scoring

@api_view(['POST'])
def predict_score(request):
    raw = JSONParser().parse(request)
    # print(raw)
    # import pdb; pdb.set_trace()
    order = scoring.OrderScore(raw)
    score = order._predict()
    return Response(score, template_name='HTMLRenderer')