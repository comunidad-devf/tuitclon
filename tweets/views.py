from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from tweets.forms import TweetForm
from tweets.models import Tweet


def new_tweet(request):
	if request.method == 'POST':
		form = TweetForm(request.POST)
		print request.POST
		return HttpResponse('')
		if form.is_valid():
			form.save()
			return HttpResponse('Guardado!')
		else:
			return render(request, 'tweets/create_tweet.html', {'tweet_form': form})

	form = TweetForm()
	return render(request, 'tweets/create_tweet.html', {'tweet_form': form})

def show_tweet(request, id_tweet):
	tweet = get_object_or_404(Tweet, id=id_tweet)	
	# try:
	# 	tweet = Tweet.objects.get(id=id_tweet)
	# except Tweet.DoesNotExist:
	# 	raise Http404('Ese Tweet no existe')

	return render(request, 'tweets/show_tweet.html', {'tweet': tweet})
