from django.shortcuts import render
import markdown2

from . import util

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# /wiki/<page> function to use get_entry() to convert page's md to HTML
def entry(request, page):
    mdown = util.get_entry(page)
    content = markdown2.markdown(mdown)
    return render(request, "encyclopedia/entry.html", {
        "title": page,
        "body": content
    })