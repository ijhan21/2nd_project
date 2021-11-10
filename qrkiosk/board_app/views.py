from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Board
from django.urls import reverse


class BoardView(LoginRequiredMixin, TemplateView):
    template_name = 'list.html'

    def board(request):
        boards = {'boards': Board.objects.all()}
        return render(request, 'list.html', boards)

class PostView(LoginRequiredMixin, TemplateView):
    template_name = 'post.html'

    def post1(request):
        if request.method == "POST":
            author = request.POST['author']
            title = request.POST['title']
            content = request.POST['content']
            board = Board(author=author, title=title, content=content)
            board.save()
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'post.html')
