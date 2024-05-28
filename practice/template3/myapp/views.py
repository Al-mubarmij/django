from django.shortcuts import render
from .models import Menu
# Create your views here.
def menu(request):
    newmenu = {'mains':[
        {'name': 'falafel', 'price': '12'},
        {'name': 'shawarma', 'price': '15'},
        {'name': 'gyro', 'price': '10'},
       
    ]}
    menuitem = {'name':'GreekSalad'}
    return render(request, 'menu.html', newmenu)
    

def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu': newmenu}
    return render(request, 'menu_card.html', newmenu_dict)

def about(request):
    context = {'about_us': 'Minim occaecat anim nulla tempor et officia est in eu laborum amet officia exercitation. Elit sint adipisicing ullamco eiusmod ipsum eu ullamco amet ea in veniam ad ut. Cupidatat Lorem aute fugiat amet ad cupidatat. Fugiat sit velit fugiat esse ipsum reprehenderit mollit labore culpa ex laborum et cupidatat.'}
    return render(request, 'about.html', context) 
