from django.shortcuts import render
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    mdown = util.get_entry(entry)
    content = markdown2.markdown(mdown)
    return render(request, "encyclopedia/entry.html", {
        "title": entry,
        "body": content
    })