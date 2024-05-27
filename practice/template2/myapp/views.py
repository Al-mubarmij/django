from django.shortcuts import render

# Create your views here.
def about(request):
    context = {'about_us': 'Nulla culpa in anim et consequat adipisicing duis Lorem fugiat occaecat. Reprehenderit mollit eiusmod pariatur id commodo velit dolor mollit labore do. Amet et consequat nostrud irure aliquip cillum cupidatat commodo enim esse qui reprehenderit. Nostrud exercitation nostrud aliqua amet sint. Veniam dolore enim sunt ipsum ea qui sunt pariatur voluptate consequat eiusmod ut dolor. Consequat consectetur veniam cillum in.'}
    return render(request, 'about.html', context)

def menu(request):
    context = {}
    return render(request, 'menu.html', context)
