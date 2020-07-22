from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
# Create your views here.


class IndexClass(View):
    def get(self, request):
        return HttpResponse('<h1>Hello</h1>')


class LoginClass(View):
    def get(self, request):
        return render(request, 'Login/login.html')

    def post(self, request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('User is not exits, Login failed')
        login(request, my_user)
        # return HttpResponse("Username and Password %s %s" % (user_name, pass_word))
        return render(request, 'Login/index.html')


class ViewUser(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        return HttpResponse('<h2>Day la view user</h2>')

    def post(self, request):
        pass


@decorators.login_required(login_url='login/')
def view_product(request):
    return HttpResponse('xem san pham')


class AddPost(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request):
        f = PostForm()
        context = {'fm': f}
        return render(request, 'Login/add_post.html', context)

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse("Nhap sai hoac vuot qua du lieu")
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_post'): #ten app.(them, sua, xoa)_ten model viet thuong
            f.save()
        else:
            return HttpResponse("Ban khong co quyen dang nhap")
        return HttpResponse("ok")
