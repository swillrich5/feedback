from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView

from .forms import ReviewForm

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form": form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/thank-you")


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
       "form": form
    })


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['message'] = "Happy trails to you!"
        return context