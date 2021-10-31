from django.shortcuts import redirect, render,HttpResponse
from django.urls.base import reverse
from django.views.generic import ListView
from core.forms import LoginForm, UserForm
from django.contrib.auth.models import  auth

from core.models import Book, User
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def index(request):
    return redirect("/book")




class BookList(ListView):
    model = Book
    template_name="book.html"
    context_object_name = 'books'

@method_decorator(login_required, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    template_name = 'addbook.html'
    fields = ('book_name', 'author_name', )
    success_url = reverse_lazy('book-list')

@method_decorator(login_required, name='dispatch')
class BookDetailView(DetailView):

    model = Book
    template_name = 'detail.html'
    context_object_name = 'book'

@method_decorator(login_required, name='dispatch')
class BookUpdateView(UpdateView):

    model = Book
    template_name = 'update.html'
    context_object_name = 'book'
    fields = ('book_name', 'author_name',)

    def get_success_url(self):
        return reverse_lazy('book-detail', kwargs={'pk': self.object.id})

@method_decorator(login_required, name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'delete.html'
    success_url = reverse_lazy('book-list')

def register_admin(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            password = request.POST['password']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return redirect("/login")
    else:
        form = UserForm()
     
    context = {
        'form': form,
     
    }
    return render(request, 'register.html', context)

def login_admin(request):
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['email']
            password = request.POST['password']
            print(username)
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                try:
                    find_user = User.objects.get(id=request.user.id)
                    return redirect('/book')
                except Exception as e:
                    raise e
            else:
                return HttpResponse("username or password is wrong")
    else:
        form = LoginForm()
    context = {
        'form': form,
     
    }
    return render(request, 'login.html',context)





def logout(request):
    auth.logout(request)
    return redirect('/book')