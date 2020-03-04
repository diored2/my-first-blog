from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html')
def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте\
                                                              мне их по телефону', '(063) 205-94-61',
                                                             'lol.lvl159@gmail.com']})
def blog(request):
    return render(request,'blog/base.html')