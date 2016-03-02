from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import json
# Create your views here.
from .models import Plant,Article

def index(request):
	plants= Plant.objects.all()
	for plant in plants:
		plant.path_picture = plant.path_picture.replace("./plants","")
	return render(request,'index.html',{'plants':plants})
	
def plant_article(request,plant_slug):
	plant = Plant.objects.get(slug=plant_slug)
	articles = plant.article_set.all()
	js_article = articles
	for article in js_article:
	#	if len(article.intro)>80:
	#		article.intro = article.intro[:80]
	#	article.intro = article.intro+"......"
		article.intro =json.dumps(article.intro)
	allplant = Plant.objects.all()
	return render(request,'plant_article.html',{'articles':js_article,'allplant':allplant})
	
	
def article_detail(request,pk,article_slug):
	article = Article.objects.get(pk=pk)
	if article_slug !=article.slug:
		return redirect(article,permanent=True)
	allarticle = Article.objects.filter(slug=article_slug)
	return render(request,'article.html',{'article':article,'allarticle':allarticle})
	


	
