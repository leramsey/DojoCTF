from django.shortcuts import render
from django.views.generic import ListView, DetailView
from hiveFeed.models import hivePost
from .forms import postCreateForm
from django.shortcuts import redirect
def index(request):
    return render(request, 'home.html')



class Feed(ListView):
    model = hivePost
    template_name = 'Feed.html'

class detail_post_View(DetailView):
    model = hivePost
    template_name = 'postView.html'



def post_create_view(request):
    form = postCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        response = redirect('/feed/')
        return response
    context = {
        'form': form
    }
    return render(request, 'createPost.html', context)
# Create your views here.
def Hidden(request):
    return render (request, 'VGhpc2lzaGlkZGVuYmlndGltZQ.html')