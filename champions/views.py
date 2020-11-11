from django.shortcuts import render
from django.views.generic import ListView, DetailView
from champions.models import Champion


class ChampionView(ListView):
    model = Champion
    template_name = "champions/list.html"
    context_object_name = "champ"


class ChampionDetailView(DetailView):

    model = Champion
    template_name = "champions/detail.html"


def search_view(request):
    champion = Champion.objects.all()
    word = request.GET.get("word")
    search_champ = champion.filter(name__icontains=word)

    return render(request, "champions/search.html", {"search_champ": search_champ})
