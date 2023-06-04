from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView


def home_page(request):
    projects = Post.objects.order_by('-date_posted')[:4]
    return render(request, 'blog/pages/home_page.html', {'projects': projects})


class ProjectPageView(ListView):
    model = Post
    template_name = 'blog/pages/projects_page.html'
    context_object_name = 'projects'
    ordering = ['-date_posted']


# def project_details_page(request):
#     return render(request, 'blog/pages/project_details.html')


class ProjectInfoView(DetailView):
    model = Post
    template_name = 'blog/pages/project_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_id = self.kwargs['pk']
        get_post = Post.objects.get(pk=get_id)
        try:
            get_albums = get_post.post_albums_fk.all()
        except:
            context['albums'] = ''
        else:
            context['albums'] = get_albums
        return context


def videos_page(request):
    return render(request, 'blog/pages/videos_page.html')


def about_me_page(request):
    return render(request, 'blog/pages/about_me_page.html')
