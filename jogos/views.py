from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Jogo, Desenvolvedora, Plataforma

def lista_jogos(request):
    # 1. Consulta inicial otimizada com select_related
    jogos_qs = Jogo.objects.select_related('desenvolvedora', 'plataforma').all()

    # 2. Captura dos parâmetros GET
    busca = request.GET.get('q', '').strip()
    desenvolvedora_id = request.GET.get('desenvolvedora', '')
    plataforma_id = request.GET.get('plataforma', '')

    # 3. Aplicação dos filtros dinâmicos (funcionam isolados ou combinados)
    if busca:
        jogos_qs = jogos_qs.filter(nome__icontains=busca)
    if desenvolvedora_id:
        jogos_qs = jogos_qs.filter(desenvolvedora_id=desenvolvedora_id)
    if plataforma_id:
        jogos_qs = jogos_qs.filter(plataforma_id=plataforma_id)

    # 4. Paginação (5 registros por página APÓS filtrar)
    paginator = Paginator(jogos_qs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # 5. Listas para preencher os <select> no HTML
    desenvolvedoras = Desenvolvedora.objects.all().order_by('nome')
    plataformas = Plataforma.objects.all().order_by('nome')

    context = {
        'page_obj': page_obj,
        'desenvolvedoras': desenvolvedoras,
        'plataformas': plataformas,
        'busca': busca,
        'desenvolvedora_selecionada': desenvolvedora_id,
        'plataforma_selecionada': plataforma_id,
    }
    return render(request, 'jogos/lista_jogos.html', context)