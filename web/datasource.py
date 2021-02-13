from web.models import *
from web.serializers import *
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from web import messages

class DataSource(object):    
    def __init__(self):
        pass

    def homeData(self):
        categories = CategorySerializer(Category.objects.all(), many=True)
        blocks = BlockSerializer(Block.objects.all(), many=True)

        return {
            "blocks": blocks.data,
            "categories": categories.data
        }

    def movieData(self, slug):
        categories = CategorySerializer(Category.objects.all(), many=True)
        movie = Movie.objects.filter(slug=slug).first()
        movieDetail = MovieDetailSerializer(MovieDetail.objects.filter(movie=movie).first())

        return {
            "movieDetail": movieDetail.data,
            "categories": categories.data
        }

    def categoryData(self, slug):
        category = Category.objects.filter(slug=slug)
        movies = MovieSerializer(Movie.objects.filter(categories__in=category), many=True)        
        categories = CategorySerializer(Category.objects.all(), many=True)

        return {
            "movies": movies.data,
            "categories": categories.data,
            "category": category.first()
        }

    def searchData(self, keyword):
        movies = MovieSerializer(Movie.objects.filter(name__icontains=keyword), many=True)        
        categories = CategorySerializer(Category.objects.all(), many=True)

        return {
            "movies": movies.data,
            "categories": categories.data
        }

    def addToList(self, parameters, user):
        if not Functions().is_valid("addToList", parameters):
            return messages.errors["invalid_request"]

        movie = Movie.objects.filter(id = parameters.get("movie_id", None))

        if movie == None:
            return messages.errors["movie_not_found"]

        w = WishList()
        w.movie = movie
        w.user = user
        w.save()

        return messages.success

    def auth(self, request):
        if not Functions().is_valid("auth", request.POST):
            return None

        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        return authenticate(request, username=username, password=password)

    def register(self, request):
        if not Functions().is_valid("register", request.POST):
            return None

        username = request.POST.get("username", None)
        password = request.POST.get("password", None)

        user = User.objects.create_user(username, username, password)
        user.save()
        return user

class Functions(object):    
    def __init__(self):
        pass

    def is_valid(self, method, data):
        if (method == "addToList"):
            if (data.get("movie_id", None) != None):
                return True

        if (method == "auth"):
            if ((data.get("username", None) != None) and (data.get("password", None) != None)):
                return True

        if (method == "register"):
            if ((data.get("username", None) != None) and (data.get("password", None) != None)):
                return True

        return False
            