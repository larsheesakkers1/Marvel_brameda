from django.shortcuts import render
from .models.comic import Comic
from marvelFinder.core.request import RequestMarvel
from django.core.paginator import Paginator 

def index(request):
    commics = []
    for c in RequestMarvel.marvelApi('comics'):
        commics.append(Comic(c['title'],c['id'],c['series'],c['characters'],c['thumbnail']['path']))
        
    paginator = Paginator(commics, 6) # < 3 is the number of items on each page
    page = request.GET.get('page') # < Get the page number
    commics = paginator.get_page(page)
    
    context = {'commics' : commics}
    return render(request, 'marvel/index.html', context) 

def detail(request, comicId):
    response = RequestMarvel.marvelApi('comics/{0}'.format(comicId))[0]
    characters = []
    
    for f in response['characters']['items']:
        id =  f['resourceURI'].split('/')[-1]
        characters.append({'name': f['name'],'id': id});
        
    data = Comic(response['title'],response['id'],response['series'],characters,response['thumbnail']['path'])
    context = {'comic' : data,"serieId" : response['series']['resourceURI'].split('/')[-1]}
    return render(request, 'marvel/detail.html', context) 