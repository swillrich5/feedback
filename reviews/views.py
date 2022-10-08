from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .forms import ReviewForm
from .models import Review

# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = "Happy trails to you!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model =  Review
    context_object_name = "reviews"

    def get_queryset(self):                         # allows to filter the data returned
        base_query = super().get_queryset()         # in this case reviews with ratings 
        data = base_query.filter(rating__gte=4)     # that are greater than or equal to 4
        return data


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
