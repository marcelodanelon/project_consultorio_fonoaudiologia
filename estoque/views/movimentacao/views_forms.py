from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from babel.numbers import format_currency
from django.core import serializers
from django.http import JsonResponse
from estoque.forms import MovimentacaoInsumoForm, ItensMovimentacaoInsumoForm, ItensInsumoForm
from estoque.models import MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, ItensInsumoModel,InsumoModel, GrupoInsumoModel

@login_required(login_url='home:loginUser')
def getJSONitem(request):
    if request.GET.get('searchLocal'):
        q = int(request.GET.get('searchLocal'))
        model = list(ItensInsumoModel.objects.filter(local=q).exclude(quantidade=0).values())
        for i in model:
            insumo = InsumoModel.objects.filter(id=i['insumo_id']).first()
            i['insumo_nome'] = insumo.descricao
        return JsonResponse(data={'results': model})

@login_required(login_url='home:loginUser')
def getJSONinsumo(request):
    if request.GET.get('searchInsumo'):
        q = int(request.GET.get('searchInsumo'))
        model = InsumoModel.objects.filter(pk=q).first()
        if model:
            model_data = serializers.serialize('json', [model])
            return JsonResponse(data={'results': model_data}, safe=False)
        else:
            return JsonResponse(data={'results': None})
    else:
        return JsonResponse(data={'results': None})

@login_required(login_url='home:loginUser')
def getJSONclient(request):
    if request.GET.get('searchClient'):
        q = int(request.GET.get('searchClient'))
        tipoMov = request.GET.get('tipoMovimentacao')
        mensagem = ""
        if tipoMov == 'doacao':
            try:
                verificandoDoacoes = MovimentacaoInsumoModel.objects.filter(tipoMovimentacao='doacao').filter(eClient=q).last()
                data = verificandoDoacoes.data.strftime('%d/%m/%Y')
                if verificandoDoacoes:
                    mensagem = f"Última data de doação em {data} com os itens: "
                    itensDaDoacao = ItensMovimentacaoInsumoModel.objects.filter(movimentacao=verificandoDoacoes.pk)
                    for item in itensDaDoacao:
                        mensagem += f'{item.insumo} '
            except:
                mensagem = ""
        model = MovimentacaoInsumoModel.objects.filter(eClient=q).first()
        if model:
            model_data = serializers.serialize('json', [model])
            return JsonResponse(data={'results': model_data, 'mensagem': mensagem}, safe=False)
        else:
            return JsonResponse(data={'results': None, 'mensagem': mensagem})
    else:
        return JsonResponse(data={'results': None})

@login_required(login_url='home:loginUser')
def getJSONgrupo(request):
    if request.GET.get('searchGrupo'):
        q = int(request.GET.get('searchGrupo'))
        model = GrupoInsumoModel.objects.filter(pk=q).first() 
        if model:
            model_data = serializers.serialize('json', [model])
            return JsonResponse(data={'results': model_data}, safe=False)
        else:
            return JsonResponse(data={'results': None})
    else:
        return JsonResponse(data={'results': None})

@login_required(login_url='home:loginUser')
def updateMovimentacaoInsumo(request, movimentacao_id):
    try:
        search = int(request.GET.get('searchLocal'))
        items = ItensMovimentacaoInsumoModel.objects.filter(local=search)
    except:
        search = None
        items = None

    form_action = reverse('estoque:updateMovimentacaoInsumo', kwargs={'movimentacao_id':movimentacao_id})
    movimentacao = get_object_or_404(MovimentacaoInsumoModel, pk=movimentacao_id)
    formMov=MovimentacaoInsumoForm(instance=movimentacao)
    formIte=inlineformset_factory(MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, form=ItensMovimentacaoInsumoForm, extra=0, can_delete=True, min_num=1)

    context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'name_screen': 'Movimentação de Insumos',
        'groups_user': list(request.user.groups.values_list('name', flat=True)),
        'items_saida': items,
        'formMovimentacao': formMov,
        'form_action': form_action,
        'isUpdate': 1,
        'formSetMovimentacao': formIte(instance=movimentacao),
    }
        
    return render(
        request,
        'estoque/movimentacao/movimentacao.html',
        context
    )

@login_required(login_url='home:loginUser')
def createMovimentacaoInsumo(request):
    form_action = reverse('estoque:createMovimentacaoInsumo')
    modelMovimentacao = MovimentacaoInsumoModel()
    formMovimentacao = MovimentacaoInsumoForm()
    formSetMovimentacao=inlineformset_factory(MovimentacaoInsumoModel, ItensMovimentacaoInsumoModel, form=ItensMovimentacaoInsumoForm, extra=0, can_delete=True, min_num=1)
    formSetMovimentacaoInsumo=inlineformset_factory(MovimentacaoInsumoModel, ItensInsumoModel, form=ItensInsumoForm, extra=0, can_delete=True, min_num=1)


    if request.method == 'POST':
        formMovimentacao = MovimentacaoInsumoForm(request.POST, instance=modelMovimentacao)
        formSetItensMovimentacao_P = formSetMovimentacao(request.POST, instance=modelMovimentacao)
        formSetItensInsumo_P = formSetMovimentacaoInsumo(request.POST, instance=modelMovimentacao)

        if formMovimentacao.is_valid() and formSetItensMovimentacao_P.is_valid():
            match formMovimentacao.cleaned_data['operacao']:
                case 'Entrada': 
                    success = True
                    model = formMovimentacao.save()
                    modelSet = formSetItensMovimentacao_P.save(commit=False)
                    modelSetInsumo = formSetItensInsumo_P.save(commit=False)

                    for item in modelSet:
                        item.local = model.local
                        item.dataEntrada = model.data
                    # replica para o Itens no cadastro do Insumo | valores e quantidades serão ajustados mais abaixo
                    for item in modelSet:
                        novo_item_insumo = ItensInsumoModel(
                            movimentacao=item.movimentacao,  
                            insumo=item.insumo,
                            valorUnitario=item.valorUnitario,  
                            valorTotal=item.valorTotal,  
                            quantidade=item.quantidade,
                            dataValidade=item.dataValidade,  
                            dataEntrada=item.dataEntrada,  
                            serie=item.serie,  
                            local=item.local,  
                        )
                        modelSetInsumo.append(novo_item_insumo)

                    insumo = None
                    insumo_valorUnitario = None
                    # verifica se há lote existente
                    for item in modelSet:
                        try:
                            insumo = ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).get()
                            insumo_valorUnitario = float(insumo.valorUnitario.replace("R$", "").replace(".", "").replace(",", ".").strip())
                            insumo_valorUnitario = format_currency(insumo_valorUnitario, 'BRL', locale='pt_BR')
                        except Exception as e:
                            insumo = None
                            print(e)

                        # retira pontos e virgulas e converte em reais
                        item_valorUnitario = float(item.valorUnitario.replace("R$", "").replace(".", "").replace(",", ".").strip())  
                        item_valorUnitario = (item_valorUnitario/100)         
                        item_valorUnitario = format_currency(item_valorUnitario, 'BRL', locale='pt_BR')

                        # verifica valor unitario divergente
                        if insumo != None and item_valorUnitario != insumo_valorUnitario:
                            messages.error(request, f'Valor Unitário para o {insumo}, diferente da série/lote existente.')
                            success = False
                            break

                    if success == True:
                        for item in modelSet:
                            # controle inclusão de entrada para lote existente ou novo 
                            if insumo:                    
                                totalQuantidade = insumo.quantidade + item.quantidade
                                valorTotal_insumo = float(insumo.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                                valorTotal_item = float(item.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                                totalValor = valorTotal_insumo + (valorTotal_item/100)
                                totalValor = format_currency(totalValor, 'BRL', locale='pt_BR')
                                ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).update(quantidade=totalQuantidade)
                                ItensMovimentacaoInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).update(valorTotal=totalValor)
                                messages.success(request, f'Lote para {insumo} já existente, adicionado quantidade na Data de Entrada: {insumo.dataEntrada}')
                            else:
                                item_valorUnitario = float(item.valorUnitario.replace(",","").replace(".",""))
                                item.valorUnitario = format_currency(item_valorUnitario / 100, 'BRL', locale='pt_BR')
                                item_valorTotal = float(item.valorTotal.replace(",","").replace(".",""))
                                item.valorTotal = format_currency(item_valorTotal / 100, 'BRL', locale='pt_BR')
                                try:
                                    item_valorCompra = float(item.valorCompra.replace(",","").replace(".",""))
                                    item.valorCompra = format_currency(item_valorCompra / 100, 'BRL', locale='pt_BR')
                                except:
                                    ...
                                item.save()

                        for item in modelSetInsumo:
                            # controle inclusão de entrada para lote existente ou novo 
                            if insumo:                    
                                totalQuantidade = insumo.quantidade + item.quantidade
                                valorTotal_insumo = float(insumo.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                                valorTotal_item = float(item.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                                totalValor = valorTotal_insumo + (valorTotal_item/100)
                                totalValor = format_currency(totalValor, 'BRL', locale='pt_BR')
                                ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).update(quantidade=totalQuantidade)
                                ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).update(valorTotal=totalValor)
                                messages.success(request, f'Lote para {insumo} já existente, adicionado quantidade na Data de Entrada: {insumo.dataEntrada}')
                            else:
                                item_valorUnitario = float(item.valorUnitario.replace(",","").replace(".",""))
                                item.valorUnitario = format_currency(item_valorUnitario / 100, 'BRL', locale='pt_BR')
                                item_valorTotal = float(item.valorTotal.replace(",","").replace(".",""))
                                item.valorTotal = format_currency(item_valorTotal / 100, 'BRL', locale='pt_BR')
                                item.save()
                        messages.success(request, 'Movimentação gravada com sucesso!')
                        return redirect('estoque:index')
                    else:

                        print(formSetItensMovimentacao_P.errors)
                        print(formSetItensInsumo_P.errors)
                case 'Saída':
                    success=None
                    model = formMovimentacao.save(commit=False)
                    modelSet = formSetItensMovimentacao_P.save(commit=False)

                    for item in modelSet:
                        item.local = model.local
                        item.dataEntrada = model.data

                    # verifica se há saldo para saída
                    for item in modelSet:
                        if success != False:
                            insumo = ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(local=item.local).filter(serie=item.serie).get()                   
                            if insumo.quantidade >= item.quantidade:
                                success=True
                            else:
                                success=False
                                break

                    # verifica se informou um usuário caso tipo seja venda
                    if model.eClient == None and model.tipoMovimentacao == 'venda':
                        messages.error(request, 'Usuário de venda não informado!')
                        success = False

                    # realiza ação e verificação
                    if success:
                        formMovimentacao.save()
                        for item in modelSet:
                            insumo = ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).filter(local=item.local).get() 
                            totalQuantidade = insumo.quantidade - item.quantidade
                            valorTotal_insumo = float(insumo.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                            valorTotal_item = float(item.valorTotal.replace("R$", "").replace(".", "").replace(",", ".").strip())
                            totalValor = valorTotal_insumo - (valorTotal_item/100)
                            totalValor = format_currency(totalValor, 'BRL', locale='pt_BR')
                            ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).update(quantidade=totalQuantidade)
                            ItensInsumoModel.objects.filter(insumo=item.insumo.pk).filter(serie=item.serie).update(valorTotal=totalValor)
                            item.save()
                        messages.success(request, f'Saída gravada com sucesso!')
                        return redirect('estoque:index')
                    else:
                        messages.error(request, f'Saldo insuficiente para insumo {insumo}!')
                        context = {
                            'title': 'Estoque',
                            'name_module': 'Estoque',
                            'form_action': form_action,
                            'name_screen': 'Movimentação de Insumos',
                            'formMovimentacao': MovimentacaoInsumoForm(),
                            'groups_user': list(request.user.groups.values_list('name', flat=True)),
                            'formSetMovimentacao': formSetMovimentacao,
                        }

                        return render(
                            request,
                            'estoque/movimentacao/movimentacao.html',
                            context
                        )
        else:
            print(formMovimentacao.errors)
            print(formSetItensMovimentacao_P.errors)

    context = {
        'title': 'Estoque',
        'name_module': 'Estoque',
        'form_action': form_action,
        'name_screen': 'Movimentação de Insumos',
        'formMovimentacao': formMovimentacao,
        'groups_user': list(request.user.groups.values_list('name', flat=True)),
        'formSetMovimentacao': formSetMovimentacao(instance=MovimentacaoInsumoModel()),
    }

    return render(
        request,
        'estoque/movimentacao/movimentacao.html',
        context
    )