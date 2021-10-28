from .models import Board, Comment
from .forms import UserRegisterForm
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import UpdateView, BaseDetailView, DeleteView, CreateView
from django.contrib import messages
from django.views import View
import time

import requests, json
import pandas as pd
from .forms import BoardForm
from django.core.exceptions import ValidationError


def home(request):
    return render(request, 'home.html')

########################################################################
###                         api                                      ###
########################################################################

# @login_required
# @csrf_exempt
class Boardapi(generic.TemplateView):
    def get(self, request):
        url = 'http://127.0.0.1:8080/boardapi/'
        datas = requests.get(url).json()

        df = pd.DataFrame(datas)
        blist = [tuple(r) for r in df.to_numpy()]

        return render(self.request, 'boardapi_list.html', {
            "board_list" : blist
            })
    

class Boardcommentapi_detail(generic.DetailView):
    def get(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk'],
        }
        # board
        url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/'

        bdetail = requests.get(url, params=datas).json()
        
        # comment
        c_url = 'http://127.0.0.1:8080/boardapi/'  + str(datas['pk']) + '/comment/'
        cdatas = requests.get(c_url, params=datas).json()

        cdf = pd.DataFrame(cdatas)
        clist = [tuple(r) for r in cdf.to_numpy()]

        return render(self.request, 'boardapi_view.html', {
            "board_detail" : bdetail,
            "comment_list" : clist 
            })

    def post(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk'],
            'c_writer' : request.POST.get('c_writer'),
            'c_note' : request.POST.get('c_note'),
        }

        url = 'http://127.0.0.1:8080/boardapi/'  + str(datas['pk']) + '/comment/'
        ccreate = requests.post(url, data=datas)

        return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))
    

def Boardapi_writeview(request):
    return render(request, 'boardapi_write.html')

# @csrf_exempt
class Boardapi_insert(generic.CreateView):
    def post(self, request):
        datas = {
            'b_title': request.POST.get('b_title'),
            'b_writer' : request.POST.get('b_writer'),
            'b_note' : request.POST.get('b_note'),
        }

        url = 'http://localhost:8080/boardapi/'
        bcreate = requests.post(url, data=datas)

        return redirect(reverse('board'))


class Boardapi_update(generic.UpdateView):
    def get(self, request, *args, **kwargs):
        data = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/'
        b_get = requests.get(url, params=data).json()

        return render(self.request, 'boardapi_edit.html', {
            'board_edit_view': b_get
        })
    
    def post(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk'],
            'b_title' : request.POST.get('b_title'),
            'b_writer' : request.POST.get('b_writer'),
            'b_note' : request.POST.get('b_note')
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(datas['pk']) + '/'
        c_update = requests.put(url, data=datas)

        return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))


class Boardapi_delete(generic.DeleteView):
    def get(self, request, *args, **kwargs):
        data = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/'
        b_get = requests.delete(url, params=data)

        return render(self.request, 'boardapi_view.html', {
            'board_detail': b_get
        })
    
    def post(self, request, *args, **kwargs):
        data = {
            'pk': self.kwargs['pk']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/'
        b_del = requests.delete(url, params=data)

        return redirect(reverse('board'))
        
    


######################  Comment ##########################


class Commentapi_delete(generic.DeleteView):
    def get(self, request, *args, **kwargs):
        data ={
            'pk': self.kwargs['pk'],
            'id': self.kwargs['id']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/comment/'
        c_get = requests.get(url, params=data)

        return render(self.reqeust, 'boardapi_view.html', {
            'comment_delete_list': c_get
        })

    def post(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk'],
            'id': self.kwargs['id']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(datas['pk']) + '/comment/' + str(datas['id']) + '/'
        c_delete = requests.delete(url, params=datas)

        return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))
    

class Commentapi_update(generic.UpdateView):
    def get(self, request, *args, **kwargs):
        data = {
            'pk': self.kwargs['pk'],
            'id': self.kwargs['id']
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/comment/'
        cdatas = requests.get(url, params=data).json()

        cdf = pd.DataFrame(cdatas, index=[0])
        clist = [tuple(r) for r in cdf.to_numpy()]

        return render(self.request, 'comment_edit.html', {
            'comment_list': clist
        })
    
    def post(self, request, *args, **kwargs):
        datas = {
            'pk': self.kwargs['pk'],
            'id': self.kwargs['id'],
            'c_writer' : request.POST.get('c_writer'),
            'c_note' : request.POST.get('c_note')
        }

        url = 'http://127.0.0.1:8080/boardapi/' + str(datas['pk']) + '/comment/' + str(datas['id']) + '/'
        c_update = requests.put(url, data=datas)

        return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))


####################### LOGIN #######################

#로그인
def Login(request):
    return render(request, 'accounts/login.html')


class LoginView(LoginView):
    template_name = 'accounts/login.html'

    def post(self, request):
        data = {
            'username' : request.POST.get('username'),
            'password' : request.POST.get('password'),
        }

        url = 'http://localhost:8080/rest-auth/login/'

        blogin = requests.post(url, data=data)

        print(data)
        print(blogin)

        url2 = 'http://localhost:8080/rest-auth/user/'
        blogin2 = requests.get(url2).json
        print(blogin2)

        return redirect('/')


# 로그아웃

def Logout(request):
    return render(request, 'accounts/logout.html')


class LogoutView(View):
    def post(self, request):
        url = 'http://localhost:8080/rest-auth/logout/'

        logout = requests.post(url)

        return redirect('/')


class SignupView(generic.CreateView):
    form = UserRegisterForm
    def get(self, request):
        url = 'http://localhost:8080/rest-auth/registration/'
        signup = requests.get(url)

        return render(self.request, 'accounts/signup.html')

    def post(self, request):
        data = {
            'username' : request.POST.get('username'),
            'email' : request.POST.get('email'),
            'password1' : request.POST.get('password1'),
            'password2' : request.POST.get('password2'),
        }

        url = 'http://localhost:8080/rest-auth/registration/'
        try:
            signup = requests.post(url, data=data)
            print('post.signup', signup)

            if signup.status_code == 400:
                error = requests.post(url, data=data).json()
                msg = messages.add_message(self.request, messages.ERROR, error)
                return redirect(reverse('signup'))
            elif signup.status_code == 200 or 201:
                messages.add_message(self.request, messages.SUCCESS, 'Success')
                # return redirect(reverse('login'))
                return redirect(reverse('login'))
            else:
                return HttpResponse('Unknown Error Occurred')

        except:
            messages.warning(self.request, "?")
            return redirect("/")

        return redirect(reverse('login'))


############# test ##################

# class xptmxm(generic.DeleteView):
#     def get(self, request, *args, **kwargs):
#         datas = {
#             'pk': self.kwargs['pk'],
#         }

#         url = 'http://127.0.0.1:8080/boardapi/'+str(datas['pk'])+'/'

#         bdetail = requests.get(url, params=datas).json()

#         c_url = 'http://127.0.0.1:8080/boardapi/'  + str(datas['pk']) + '/comment/'
#         cdatas = requests.get(c_url, params=datas).json()

#         print(cdatas)

#         cdf = pd.DataFrame(cdatas)

#         clist = [tuple(r) for r in cdf.to_numpy()]

#         return render(self.request, 'boardapi_view.html', {
#             "board_detail" : bdetail,
#             "comment_list" : clist
#             })

#     def post(self, request, *args, **kwargs):
#         datas = {
#             'pk': self.kwargs['pk'],
#         }

#         url = 'http://127.0.0.1:8080/boardapi/' + str(datas['pk']) + '/comment/' + str(datas['pk']) + '/delete/'
#         c_delete = requests.delete(url, params=datas)

#         print(datas)
#         print(c_delete)

#         return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))
    

# class test2(generic.DeleteView):
#     def get(self, request, *args, **kwargs):
#         data ={
#             'pk': self.kwargs['pk']
#         }

#         url = 'http://127.0.0.1:8080/boardapi/' + str(data['pk']) + '/comment/'
#         c_get = requests.get(url, params=data).json()

#         return render(self.reqeust, 'test2.html', {
#             'comment_list': c_get
#         })

#     def post(self, request, *args, **kwargs):
#         datas = {
#             'pk': self.kwargs['pk']
#         }

#         url = 'http://127.0.0.1:8080/boardapi/' + str(datas['pk']) + '/comment/' + str(datas['id']) + '/delete/'
#         c_delete = requests.delete(url, params=datas)

#         print(datas)
#         print(c_delete)

#         return redirect(reverse('board_detail', kwargs={'pk': self.kwargs['pk']}))
    