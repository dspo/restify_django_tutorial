# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
#
#
# from .models import Poll, Choice
# from .serializers import PollSerializer
#
#
# class PollList(APIView):
#     def get(self, request):
#         polls = Poll.objects.all()[:20]
#         serialized = PollSerializer(polls, many=True)
#         return Response(data={'count': len(serialized.data), 'data': serialized.data})
#
#
# class PollDetail(APIView):
#     def get(self, request, pk):
#         poll = get_object_or_404(Poll, pk=pk)
#         serialized = PollSerializer(poll)
#         return Response(data=serialized.data)
#
from rest_framework import generics

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer

