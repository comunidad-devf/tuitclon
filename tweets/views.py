from django.shortcuts import render
from django.http import HttpResponse

from tweets.forms import TweetForm


def new_tweet(request):
	if request.method == 'POST':
		form = TweetForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponse('Guardado!')
		else:
			return render(request, 'tweets/create_tweet.html', {'tweet_form': form})

	form = TweetForm()
	return render(request, 'tweets/create_tweet.html', {'tweet_form': form})

