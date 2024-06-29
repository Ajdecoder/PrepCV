from django.shortcuts import render
from config import DB_INSTANCE
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bson import ObjectId
from django.http import JsonResponse, HttpResponseBadRequest


class ResumeDataView(APIView):
    def get(self, request):
        resume_id = request.GET.get("resume_id",None)
        data = DB_INSTANCE["resume_data"].find_one({"resume_id": resume_id},{"_id":0})
        if data and resume_id:
            # if '_id' in data and isinstance(data['_id'], ObjectId):
            #     data['_id'] = str(data['_id'])
            print(data.get("username"))
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Resume data not found"}, status=status.HTTP_404_NOT_FOUND)
