from django.shortcuts import render, redirect
from myapp.forms import ItemForm
from myapp.models import Item

# Create your views here.


def shopfirst(request):
    '''
    shopfirst.htmlを表示する
    DBに保存も行う
    '''
    items = Item.objects.all()

    # itemsのpriceカラムとquantityカラムをかけた値をtotalに入れる

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.total = item.price * item.quantity  # 合計値を計算してtotalに格納
            item.save()
            return redirect('shopfirst')  # shopfirstのURLにリダイレクトする
    else:
        form = ItemForm()

    total = sum(item.total for item in items) # 合計値を計算

    return render(request, 'myapp/shopfirst.html', context={
        'form': form,
        'items': items,
        'total': total
    })
