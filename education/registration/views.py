from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView


def signup(request):
    """3арегистрировать новую учетную запись пользователя"""

    #Если пользователь уже вошел в систему, мы перенаправим его со
    # страницы регистрации
    if request.user.is_authenticated:
        return redirect('/')

    #POST, это означает, что форма для создания пользователя уже
    #заполнена и пора создавать пользователя
    if request.method == 'POST':

        #Сначала создайте объект формы на серверной части с
        #данными, предоставленными пользователем
        form = UserCreationForm(request.POST)

        #Если форма действительна, создайте пользователя и войдите
        #в систему, а затем отправьте на главную страницу.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            #выгрузите их обратно на страницу создания пользователя
            #с информацией о том, какие данные были недопустимыми
            return render(request, 'signup.html', {'form': form})
    else:
        #пользователь обращается к странице впервые и должен
        #встретиться с формой для создания новой учетной записи.
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    """вход в аккаунт"""

    #Если пользователь уже вошел в систему, мы перенаправим его со
    #страницы входа
    if request.user.is_authenticated:
        return render(request, 'homepage.html')

    #POST, это означает, что форма для входа заполнена и пора
    #аутентифицировать пользователя в учетной записи.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        #Если имя пользователя и пароль соответствуют учетной записи,
        #войдите в систему
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            #верните их на страницу входа с предварительно заполненными
            #данными формы
            form = AuthenticationForm(request.POST)
            return render(request, 'signin.html', {'form': form})
    else:
        #обращается к странице впервые и должен встретиться с формой
        #для входа в систему
        form = AuthenticationForm()
        return render(request, 'signin.html', {'form': form})

def signout(request):
    """пользователи могут в конечном итоге выйти из системы"""

    logout(request)
    return redirect('/')






class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

