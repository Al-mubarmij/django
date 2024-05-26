from django.shortcuts import render
from .forms import BlogForm

# Create your views here.
def blog_form(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
    form = BlogForm()
    context = {'blogform': form}
    return render(request, 'blog.html', context)
