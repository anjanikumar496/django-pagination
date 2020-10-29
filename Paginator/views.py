from django.shortcuts import render
from django.views.generic.list import ListView


# Create your views here.
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    user_list = User.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'core/user_list.html', { 'users': users })


class UserListView(ListView):
    model = User
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = User.objects.all()  # Default: Model.objects.all()



# def index(request):
#     for i in range(1,55):
#         usernm = "user"+str(i)
#         usr = User.objects.create(username=usernm,email='jon@doe.com')
#         usr.set_password("asdqwe123")
#         usr.save()
#     return render(request, 'core/user_list.html')