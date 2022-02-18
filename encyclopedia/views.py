from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# /wiki/<page> function to use get_entry() to render page's markdown to HTML
def entry(request, page):
    try:
        content = markdown2.markdown(util.get_entry(page))
        return render(request, "encyclopedia/entry.html", {
            "title": page,
            "body": content
        })
    except: 
        return render(request, "encyclopedia/page_not_found.html")

# Search function for getting query from form
def search(request):   
    search_string = request.GET['q']
    # Redirect to entry
    if(util.get_entry(search_string) is not None):
        return HttpResponseRedirect(reverse("page", kwargs={'page': search_string }))
    # Display search_string results    
    else:
        results = []
        for i in util.list_entries():
            if search_string.lower() in i.lower():
                results.append(i)

        return render(request, "encyclopedia/results.html", {
        "entries": results
    })