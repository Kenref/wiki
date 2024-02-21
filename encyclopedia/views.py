from django.shortcuts import render, redirect
from django import forms
from random import choice

from . import util

class NewTaskForm(forms.Form):
    page = forms.CharField(label="New Page")
    content = forms.CharField(label="Content")

class EditTaskForm(forms.Form):
    content = forms.CharField(label="Edit Page Content", widget=forms.Textarea(attrs={'rows': 10, 'cols': 50, 'style': 'width: auto; height: auto;'}))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    content = util.get_entry(page)
    return render(request, "encyclopedia/page.html", {
        "page": page,
        "content": content,
    })
    
def search(request):
    query = request.GET.get('q', '')
    content = util.get_entry(query) 
    return render(request, "encyclopedia/page.html", {
        "content": content
    })

def new_page(request): 
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            page = form.cleaned_data["page"]
            content = form.cleaned_data["content"]
            util.save_entry(page, content)
            return render(request, "encyclopedia/page.html", {
                "page": page,
                "content": content,
            })
    return render(request, "encyclopedia/new_page.html", {
        "form": NewTaskForm()
    })

def edit_page(request,page):
    if request.method == "POST":
        form = EditTaskForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(page, content)
            return render(request, f"encyclopedia/page.html", {
                "page": page,
                "content": content,
            })

    content = util.get_entry(page)
    return render(request, "encyclopedia/edit_page.html", {
        "form": EditTaskForm(),
        "page": page,
        "content": content
    })

def random_page(request):
    entries = util.list_entries()

    random_page = choice(entries)
    random_content = util.get_entry(random_page)
    return render(request, "encyclopedia/page.html", {
        "page": random_page,
        "content": random_content,
    })
