from django.shortcuts import render
from django.http import HttpResponseRedirect
from models import shortenedURL, urlForm
from URLShortener.settings import WEB_PATH
# Create your views here.

def create(request):
	if (request.method=="POST"):
		form = urlForm(request.POST)
		if form.is_valid():
			try:
				query = shortenedURL.objects.get(longurl=form.cleaned_data['longurl'])
				return HttpResponseRedirect("{0}/{1:x}/info".format(WEB_PATH,query.id))
			except shortenedURL.DoesNotExist:
				newURL=shortenedURL(longurl=form.cleaned_data['longurl'])
				newURL.save()			
				return HttpResponseRedirect("{0}/{1:x}/info".format(WEB_PATH,newURL.id))
		
	else:
		form=urlForm()
	return render(request, 'create.html',{'form' : form,})

def urlprocessor(request,str_id,util):
	int_id = int(str_id,base=16)
	query =  shortenedURL.objects.get(id=int_id)
	shorturl="{0}/{1:x}".format(WEB_PATH,query.id)
	if util=='info':
		return render(request, 'success.html', {'shorturl':shorturl, 'longurl': query.longurl})
	if util =='':
		return HttpResponseRedirect(query.longurl)
