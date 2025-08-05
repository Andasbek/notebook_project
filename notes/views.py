from django.shortcuts import render

CATEGORIES = ["work", "study", "sport", "personal"]

def notes_home(request):
    return render(request, 'notes/home.html')

def all_notes(request):
    return render(request, 'notes/all_notes.html')

def category_notes(request, category):
    return render(request, 'notes/category_notes.html', {'category': category})

def note_detail(request, note_id):
    return render(request, 'notes/note_detail.html', {'note_id': note_id})

def category_list(request):
    return render(request, 'notes/category_list.html', {"categories": CATEGORIES})