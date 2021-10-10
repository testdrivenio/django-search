from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.decorators.cache import cache_page

from .models import Quote


@method_decorator(cache_page(60 * 5), name="dispatch")
class QuoteList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "quote.html"


# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"


# Q objects
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Quote.objects.filter(
#             Q(name__icontains=query) | Q(quote__icontains=query)
#         )


# Single Field Search
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Quote.objects.filter(quote__search=query)


# Multi Field Search
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         return Quote.objects.annotate(search=SearchVector("name", "quote")).filter(
#             search=query
#         )


# Stemming and Ranking
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("name", "quote")
#         search_query = SearchQuery(query)
#         return (
#             Quote.objects.annotate(
#                 search=search_vector, rank=SearchRank(search_vector, search_query)
#             )
#             .filter(search=search_query)
#             .order_by("-rank")
#         )


# Weights
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("name", weight="B") + SearchVector(
#             "quote", weight="A"
#         )
#         search_query = SearchQuery(query)
#         return (
#             Quote.objects.annotate(rank=SearchRank(search_vector, search_query))
#             .filter(rank__gte=0.3)
#             .order_by("-rank")
#         )


# Preview
# class SearchResultsList(ListView):
#     model = Quote
#     context_object_name = "quotes"
#     template_name = "search.html"

#     def get_queryset(self):
#         query = self.request.GET.get("q")
#         search_vector = SearchVector("name", "quote")
#         search_query = SearchQuery(query)
#         search_headline = SearchHeadline("quote", search_query)
#         return Quote.objects.annotate(
#             search=search_vector,
#             rank=SearchRank(search_vector, search_query)
#         ).annotate(headline=search_headline).filter(search=search_query).order_by("-rank")


# SearchVectorField
class SearchResultsList(ListView):
    model = Quote
    context_object_name = "quotes"
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Quote.objects.filter(search_vector=query)
