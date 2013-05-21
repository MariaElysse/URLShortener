from django.db import models
from django.forms import ModelForm
# Create your models here.
class shortenedURL(models.Model):
	longurl = models.URLField()

	def __unicode__(self):
		return self.longurl
	

class urlForm(ModelForm):
	class Meta:
		model = shortenedURL
		fields = ('longurl',)
