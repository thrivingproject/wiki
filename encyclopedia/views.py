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
def view_page(request, page_name):
    # If page exists
    try:
        content = markdown2.markdown(util.get_entry(page_name))
        return render(request, "encyclopedia/page.html", {
            "page_name": page_name,
            "body": content
        })
    # Does not exist
    except: 
        return render(request, "encyclopedia/page_not_found.html", {
            "page_name": page_name
        })

# Search
def search(request):   
    search_string = request.GET['q']
    results = []
    # Populate array with entries that match search string
    for i in util.list_entries():
        if search_string.lower() in i.lower():
            results.append(i)
    # Redirect to page or page not found
    if util.get_entry(search_string) is not None or not len(results):
       return view_page(request, search_string)
    # Display search results    
    else:
        return render(request, "encyclopedia/results.html", {
        "entries": results
        })
       
def edit_page(request):
    return render(request, "encyclopedia/edit.html")