# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

try:
    from tags.models import Tag
except Exception:
    Tag = None


# Create your views here.
# def show_tags(request):
#     context = {
#         "tags": Tag.objects.all() if Tag else None,
#     }
#     return render(request, "tags/list.html", context)


class TagListView(ListView):
    model = Tag
    template_name = "tags/list.html"


class TagCreateView(CreateView):
    model = Tag
    template_name = "tags/new.html"
    fields = ["name", "recipes"]
    success_url = reverse_lazy("tag_list")


class TagDetailView(DetailView):
    model = Tag
    template_name = "tags/detail.html"


class TagUpdateView(UpdateView):
    model = Tag
    template_name = "tags/edit.html"
    fields = ["name", "recipes"]
    success_url = "/"  # reverse_lazy("tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "tags/delete.html"
    success_url = "/"  # reverse_lazy("tag_list")
