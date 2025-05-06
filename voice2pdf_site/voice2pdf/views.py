from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import PdfForm
from .models import Voice2Pdf


def index(request):
    item_list = Voice2Pdf.objects.order_by("-date")
    if request.method == "POST":
        form = PdfForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voice2pdf')
    form = PdfForm()

    page = {
        "forms": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'voice2pdf/index.html', page)


def remove(request, item_id):
    item = Voice2Pdf.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('voice2pdf')
