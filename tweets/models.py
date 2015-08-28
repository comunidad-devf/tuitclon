from django.db import models


class Tweet(models.Model):
	user = models.CharField(max_length=15)
	tweet = models.CharField(max_length=140)
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return "{0} - {1}".format(self.user, self.date)