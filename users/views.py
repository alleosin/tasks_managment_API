from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
# Create your views here.


class GetUserInfoView(APIView):
    def get(self, request):
        queryset = Profile.objects.all()
        serializer_for_queryset = ProfileSerializer(
            instance=queryset,
            many=True
        )
        return Response(serializer_for_queryset.data)
