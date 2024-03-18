from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render
from .models import Tweet
from .forms import TweetForm

def tweet_list(request):
    form = TweetForm()
    tweets = Tweet.objects.all()

    if request.method == "POST":
        if request.user.is_authenticated:
            form = TweetForm(request.POST)
            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.author = request.user
                tweet.save()
                return redirect("tweet_list")
            else:
                return HttpResponseForbidden("You must be logged in to post tweets.")
    return render(request, 'index.html', {'tweets': tweets, 'form': form})