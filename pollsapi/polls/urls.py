from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from .apiviewsets import PollViewSet, ChoiceList, CreateVote


router = DefaultRouter()
router.register(prefix='polls', viewset=PollViewSet, base_name='polls')

urlpatterns = format_suffix_patterns([
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name=ChoiceList.name),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name=CreateVote.name)
])\
              + router.urls  # path('', include(router.urls)),
