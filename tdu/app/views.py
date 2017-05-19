import csv
from io import TextIOWrapper, StringIO
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import generic
from .models import Post, Category


class IndexView(generic.ListView):
    model = Post


def csv_import(request):
    form_data = TextIOWrapper(
        request.FILES['csv'].file, encoding='utf-8')
    if form_data:
        csv_file = csv.reader(form_data)
        for line in csv_file:
            post, _ = Post.objects.get_or_create(pk=line[0])
            post.title = line[1]
            post.text = line[2]
            post.sub = line[3]
            category, _ = Category.objects.get_or_create(name=line[4])
            post.category = category
            post.save()

    return redirect('app:index')


def csv_export(request):
    memory_file = StringIO()
    writer = csv.writer(memory_file)
    for post in Post.objects.all():
        row = [post.pk, post.title, post.text, post.sub, post.category.name]
        writer.writerow(row)
    response = HttpResponse(
        memory_file.getvalue(), content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=db.csv'
    return response
