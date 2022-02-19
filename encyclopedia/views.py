from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import markdown2

from . import util

# Index
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# Page
def view_page(request, search_string):
    # If page exists
    try:
        content = markdown2.markdown(util.get_entry(search_string))
        return render(request, "encyclopedia/page.html", {
            "title": search_string,
            "body": content
        })
    # Does not exist
    except: 
        return render(request, "encyclopedia/page_not_found.html", {
            "search_string": search_string
        })

# Search
def search(request):   
    search_string = request.GET['q']
    # Redirect to entry
    if(util.get_entry(search_string) is not None):
        return HttpResponseRedirect(reverse("page", kwargs={'page': search_string }))
    # Display search_string results    
    else:
        results = []
        # Check if search string matches entries
        for i in util.list_entries():
            if search_string.lower() in i.lower():
                results.append(i)
        # Search results found        
        if len(results):
            return render(request, "encyclopedia/results.html", {
            "entries": results
            })
        # No results found
        else:
            return view_page(request, search_string)
        

# Edit
def edit(request):
    return render(request, "encyclopedia/edit.html", {
        "entries": util.list_entries()
    })