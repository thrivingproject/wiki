from django.shortcuts import render
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    md = util.get_entry(entry)
    if md:
        html = markdown2.markdown(md)
        return render(request, "encyclopedia/layout.html", {
            "title": entry,
            "content": html
    })