from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
import json
import requests
#from myapi.models import TopStories, DetailStory
#from myapi.serializers import StorySerializer

# CACHE
from django.core.cache import cache

# defaul page. not used
def index(request):
    return HttpResponse("Hello, world.")

# show http response with list of top stories. check cache first and otherwise call api request
@api_view(['GET'])
def get_index_list(request):
    # GET INDEX LIST.
    if cache.get("cache_top_stories"):   #check cache
        top_stories = cache.get("cache_top_stories")
        print("top stories from cache")
        return HttpResponse(json.dumps(top_stories), status=200)
    else:
        top_stories = get_top_stories()    # call API
        if top_stories:
            cache.set("cache_top_stories", top_stories, 180)
            print("top stories from request")
            return HttpResponse(json.dumps(top_stories))
        else:
            return HttpResponse('Error, list index not found.', status=404)


# get stories by index.
@api_view(['GET'])
def get_story_by_index(request):
    # GET INDEX LIST.
    data = []
    #print(StorySerializer())
    if request.query_params:   # get i and n params
        i = request.query_params['i']
        n = request.query_params['n']

        if cache.get("cache_top_stories"):  # check cache looking for list of top stories
            top_stories = cache.get("cache_top_stories")
            print("top stories from cache")
        else:
            top_stories = get_top_stories()  # get top storis from API an save then in cache for 30 seconds
            cache.set("cache_top_stories", top_stories, 30)
            print("top stories from request")

        for det in range(int(n)): # print and save story detail
            # Search in cache first.
            index = top_stories[int(i)+int(det)]
            cache_obj = from_cache(index)
            if cache_obj:
                data.append(cache_obj)
            else:
                # Making the request.
                response = requests.get(f'https://hacker-news.firebaseio.com/v0/item/{index}.json?print=pretty')
                if response.ok:
                    # save in cache.
                    cache.set(index, response.json(), 10)
                    data.append({'Titulo': response.json()['title'], 'ID': response.json()['id']})
                    print(f'item from request: {index}')
                else:
                    return HttpResponse('Error, index not found.', status=404)

        return HttpResponse(json.dumps(data), status=200)
    else:
        return HttpResponse('Error, id is required.', status=400)


# check redis server status. show keys data in cache
@api_view(['GET'])
def redis_healthcheck(request):
    return HttpResponse(json.dumps({"keys": cache.keys("*")}), status=200)

# check if a data index by 'id' is in cache memory.
def from_cache(id):
    json_object = cache.get(id)
    if json_object != None:
        print(f'item from cache: {id}')
        return ({'Titulo': json_object['title'], 'ID': json_object['id']})
    else:
        return None


# get top stories index list
def get_top_stories():
    # GET INDEX LIST.
    response = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
    if response.ok:
        key_data = [item for item in response.json()]
        return key_data
    else:
        return None