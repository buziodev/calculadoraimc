from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario, Historico
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        nascimento = request.POST.get('nascimento', '')
        peso = float(request.POST.get('peso', 0))
        altura = float(request.POST.get('altura', 0))
        sexo = request.POST.get('sexo', '')

        if not nome or not nascimento or peso <= 0 or altura <= 0 or not sexo:
            messages.error(request, 'Todos os campos são obrigatórios e devem conter valores válidos.')
            return render(request, 'cadastro.html')


        Usuario.objects.create(
            nome=nome,
            nascimento=nascimento,
            peso=peso,
            altura=altura,
            sexo=sexo
        )
        
        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('index')

    return render(request, 'cadastro.html')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('calculadora')
        else:
            messages.error(request, 'Credenciais inválidas.')
            return redirect('login')

    return render(request, 'login.html')

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('index')

def calculadora(request):
    #if not request.user.is_authenticated:
    #    return redirect('login')

    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        data_atual = request.POST.get('data_atual', '')
        peso = float(request.POST.get('peso', 0))
        altura = float(request.POST.get('altura', 0))
        
        if not nome or not data_atual or peso <= 0 or altura <= 0:
            messages.error(request, 'Todos os campos são obrigatórios e devem conter valores válidos.')
            return render(request, 'calculadora.html')

        imc = round(peso / (altura * altura), 2)
        
        if imc < 18.5:
            status = 'Abaixo do peso'
        elif imc < 24.9:
            status = 'Peso normal'
        elif imc < 29.9:
            status = 'Sobrepeso'
        else:
            status = 'Obesidade'

        if 'salvar_historico' in request.POST:
            Usuario.objects.filter(usuario=request.user).update(
                peso=peso,
                altura=altura,
            )
            messages.success(request, 'IMC calculado e histórico salvo com sucesso!')

        return render(request, 'calculadora.html', {
            'imc': imc,
            'status': status,
        })

    return render(request, 'calculadora.html')


from django.core.paginator import Paginator


@login_required
def historico(request):
   
    historicos = Historico.objects.filter(usuario=request.user).order_by('-data')

    paginator = Paginator(historicos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'historico.html', {'page_obj': page_obj})


def salvar_imc(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        data_atual = request.POST.get('data_atual')
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))
        imc = float(request.POST.get('imc'))
        status = request.POST.get('status')

        Historico.objects.create(
            usuario = request.user,
            nome = nome,
            peso = peso,
            altura = altura,
            imc = imc,
            status = status,
            data = data_atual
        )

        messages.success(request, 'Usuário cadastrado com sucesso!')
        return redirect('calculadora')

    return render(request, 'calculadora.html')
@login_required

def grafico_historico(request):
    historicos = Historico.objects.filter(Usuario=request).order_by('data')

    labels = [h.data.strftime('%d/%m/%Y') for h in historicos]
    valores = [h.imc for h in historicos]

    return render(request, 'grafico_historico.html', {
        'labels': labels,
        'valores': valores
    })




