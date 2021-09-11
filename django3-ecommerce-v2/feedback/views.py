from django.shortcuts import render, redirect
from .forms import FeedBackForm
from django.views.generic import View


class FeedBackView(View):
    def post(self, request):
        form = FeedBackForm(request.POST)
        if form.is_valid():
            new_feedback = form.save(commit=False)
            new_feedback.phone = form.cleaned_data['phone']
            new_feedback.description = form.cleaned_data['description']
            new_feedback.save()
        return redirect('/')
