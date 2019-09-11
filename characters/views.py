from django.shortcuts import render
from .models.characters import Character
from marvelFinder.core.request import RequestMarvel
from django.core.paginator import Paginator 

def index(request):
    data = []
    for c in RequestMarvel.marvelApi('characters'):
        data.append(Character(c['id'],c['name'],c['comics'],""))

    paginator = Paginator(data, 6) # < 3 is the number of items on each page
    page = request.GET.get('page') # < Get the page number
    data = paginator.get_page(page)
    
    context = {'characters' : data}
    return render(request, 'characters/index.html', context) 

def detail(request,characterId):
    response = RequestMarvel.marvelApi('characters/{0}'.format(characterId))[0]
    comics = []
    for f in response['comics']['items']:
        id =  f['resourceURI'].split('/')[-1]
        comics.append({'name': f['name'],'id': id});
        
    data = Character(characterId,response['name'],comics,response['thumbnail']['path'] + ".jpg")
    context = {'character' : data}
    return render(request, 'characters/detail.html', context) 