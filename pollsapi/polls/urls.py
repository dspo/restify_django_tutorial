from django.urls import path
# from .views import polls_list, polls_detail
from .apiview import PollList, PollDetail, ChoiceList, CreateVote


urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path('polls/<int:pk>/choices', ChoiceList.as_view(), name=ChoiceList.name),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name=CreateVote.name)
]
