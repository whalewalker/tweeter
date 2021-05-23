from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import TweetForm
from .models import Tweet


# Create your views here.
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(data=request.POST)

        if form.is_valid():
            form.save()
            form = TweetForm()
    else:
        form = TweetForm()

    tweets = Tweet.objects.all()
    context = {
        "form": form,
        "tweets": tweets
    }
    return render(request, "tweets/index.html", context)


def detail_tweet(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    context = {'tweet': tweet}
    return render(request, 'tweets/detail_view.html', context)


def update_tweet(request, pk):
    tweet_to_update = get_object_or_404(Tweet, pk=pk)

    form = TweetForm(request.POST or None, instance=tweet_to_update)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + str(pk))

    context = {
        "form": form
    }

    return render(request, "tweets/update_view.html", context)


def delete_tweet(request, pk):
    tweet_to_delete = get_object_or_404(Tweet, pk=pk)

    if request.method == 'POST':
        tweet_to_delete.delete()

        return HttpResponseRedirect("/")
    return render(request, "tweets/delete_view.html")
