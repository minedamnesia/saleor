from django.http import HttpResponseRedirect
from django.shortcuts import render

from community.models import Story
from .forms import StoryForm


def index(request):
    story_form = StoryForm()

    if request.method == 'POST':
        story_form = StoryForm(request.POST, request.FILES)

        if story_form.is_valid():
            story_form = story_form.save(commit=False)
            if request.user.is_authenticated:
                story_form.user = request.user
            story_form.save()
            return HttpResponseRedirect("/")
    stories = Story.objects.filter(is_featured=True).order_by('-modified_at').all()
    return render(request, 'community/community.html',
                  {'story_form': story_form, 'stories': stories})
