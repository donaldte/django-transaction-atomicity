from decimal import Decimal
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render

from apps.form import AccountForm
from apps.models import Account
from django.db import transaction

# Create your views here.








def transationAtomic(request):
    form = AccountForm()
    if request.method == 'POST':
        form = AccountForm(data=request.POST)
        if form.is_valid():
            a = form.cleaned_data.get('name')
            b = form.cleaned_data.get('receiver')
            c = Decimal(form.cleaned_data.get('amount'))
            with transaction.atomic():
                sender = Account.objects.get(name=a)
                sender.amount -=c
                sender.save()

                receiver = Account.objects.get(name=b)
                receiver.amount += c 
                receiver.save()

            # Account.objects.get(name=a).update(amount=F('amount')-c)
            # Account.objects.get(name=b).update(amount=F('amount')+c)

            return HttpResponseRedirect('/')
        else:
            form = AccountForm()

    return render(request, 'index.html', {'form': form})            

       