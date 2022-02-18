from django.shortcuts import render
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