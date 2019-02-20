from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
# from .views import polls_list, polls_detail
# from .apiview import PollList, PollDetail, ChoiceList, CreateVote
from .apiviewsets import PollViewSet, ChoiceList, CreateVote


router = DefaultRouter()
router.register(prefix='polls', viewset=PollViewSet, base_name='polls')

urlpatterns = [
    # path("polls/", PollList.as_view(), name="polls_list"),
    # path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    # path('', include(router.urls)),
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name=ChoiceList.name),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name=CreateVote.name)
]

urlpatterns += router.urls  # path('', include(router.urls)),
urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
