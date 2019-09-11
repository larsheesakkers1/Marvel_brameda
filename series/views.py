from django.shortcuts import render
from .models.series import Serie
from marvelFinder.core.request import RequestMarvel
from django.core.paginator import Paginator 

def index(request):
    series = []
    for c in RequestMarvel.marvelApi('series'):
        series.append(Serie(c['id'],c['title'],c['description'],c['startYear'],c['endYear'],c['rating'],c['creators'],c['characters'],c['stories'],c['stories'],c['thumbnail']['path'] + ".jpg"))
   
    paginator = Paginator(series, 6) # < 3 is the number of items on each page
    page = request.GET.get('page') # < Get the page number
    series = paginator.get_page(page)
    
    context = {'series' : series}
    return render(request, 'series/index.html', context) 

def detail(request,serieId):
    response = RequestMarvel.marvelApi('series/{0}'.format(serieId))[0]
    comics = []
    characters = []
    for f in response['comics']['items']:
        id =  f['resourceURI'].split('/')[-1]
        comics.append({'name': f['name'],'id': id});
    for f in response['characters']['items']:
        id =  f['resourceURI'].split('/')[-1]
        characters.append({'name': f['name'],'id': id});
    
    
    data = Serie(serieId,response['title'],response['description'],response['startYear'],response['endYear'],response['rating'],response['creators'],characters,response['stories'],comics,response['thumbnail']['path'] + ".jpg")
    context = {'serie' : data}
    return render(request, 'series/detail.html', context) 