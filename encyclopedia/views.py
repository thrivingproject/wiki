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

# Entry
def view_entry(request, page_name):
    # If an entry is requested that does not exist, indicate requested page dne
    if util.get_entry(page_name) is None:
        return render(request, "encyclopedia/page_not_found.html", {
        "page_name": page_name.capitalize()
    }) 
    # Present page that displays the content of the entry with matching title
    content = markdown2.markdown(util.get_entry(page_name))
    return render(request, "encyclopedia/page.html", {
        "page_name": page_name,
        "body": content
    })

# Search
def search(request):   
    search_string = request.GET['q']
    results = []
    # Populate array with entries that match search string
    for i in util.list_entries():
        if search_string.lower() in i.lower():
            results.append(i)
    # Redirect to page or page not found if search string matches no entries
    if util.get_entry(search_string) is not None:
       return view_entry(request, search_string)
    # Display search results    
    else:
        if not len(results):
            message = "No results found"
        else:
            message = ""
        return render(request, "encyclopedia/results.html", {
            "entries": results,
            "message": message
            })

# Edit       
def edit_page(request, page_name):
    content = markdown2.markdown(util.get_entry(page_name))
    return render(request, "encyclopedia/edit.html", {
            "page_name": page_name,
            "body": content
        })

# New       
def new_page(request):
    content = ""
    page_name = ""
    return render(request, "encyclopedia/new.html", {
            "body": content,
            "page_name": page_name
        })

# Save
def save_page(request, page_name):
    content = request.POST['content']
    util.save_entry(page_name, content)
    return HttpResponseRedirect("/wiki/"+page_name+"/")

# Save new page
def save_new_page(request):
    page_name = request.POST['page_name']
    content = request.POST['content']
    util.save_entry(page_name, content)
    return HttpResponseRedirect("/wiki/"+page_name+"/")

