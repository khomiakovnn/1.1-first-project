import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination.settings import BUS_STATION_CSV


def index(request):
    return redirect(reverse('bus_stations'))


CONTENT = []
counter = 0
with open(BUS_STATION_CSV, encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        if counter !=0:
            rowdict = {
                "Name": row[1],
                "Street": row[4],
                "District": row[6]
            }
            CONTENT.append(rowdict)
        counter += 1


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
