from django.urls import path

from .views import QuoteList, SearchResultsList

urlpatterns = [
    path("", QuoteList.as_view(), name="all_quotes"),
    path("search/", SearchResultsList.as_view(), name="search_results"),
]
