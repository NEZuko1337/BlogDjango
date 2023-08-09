from django.shortcuts import render, get_object_or_404
from . import models
def all_blogs(request):
    DataBase = models.BlogModel.objects.all()
    cnt = 0
    for post in DataBase:
        if post.title != None:
            cnt+=1
            # print(post.title, post.description, post.pk)
            # print(cnt)
    return render(request, "blog/all_blogs.html", {"objects": DataBase, "cnt": cnt})

def details(request, pk):
    blog = get_object_or_404(models.BlogModel, pk = pk)
    return render(request, "blog/detail.html", {"blog":blog})