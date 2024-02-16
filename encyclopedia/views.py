from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    try:
        info = util.get_entry(page)
        body = info.split("\n", 2)[2]
    except:
        return render(request, f"encyclopedia/page.html", {
        "title": page,
        "body": "No page found"
    })    
    else:
        return render(request, f"encyclopedia/page.html", {
            "title": page,
            "body": body
        })
    
def search(request):
    query = request.GET.get('q', '')
    try:
        info = util.get_entry(query)
        body = info.split("\n", 2)[2]
    except:
        return render(request, f"encyclopedia/page.html", {
        "title": query,
        "body": "No page found"
    })    
    else:
        return render(request, f"encyclopedia/page.html", {
            "title": query,
            "body": body
        })