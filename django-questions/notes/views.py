from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Note


# READ - Display all notes (equivalent to index.php)
def index(request):
    notes = Note.objects.all()  # Already ordered by -id in model Meta
    return render(request, 'notes/index.html', {'notes': notes})


# CREATE - Add new note (equivalent to add.html + addAction.php)
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        # Validation
        errors = []
        if not title:
            errors.append('Title field is empty.')
        if not description:
            errors.append('Description field is empty.')

        if errors:
            return render(request, 'notes/add.html', {'errors': errors})

        # Create note
        Note.objects.create(title=title, description=description)
        messages.success(request, 'Data added successfully!')
        return redirect('notes:index')

    return render(request, 'notes/add.html')


# UPDATE - Edit note (equivalent to edit.php + editAction.php)
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        description = request.POST.get('description', '').strip()

        # Validation
        errors = []
        if not title:
            errors.append('Title field is empty.')
        if not description:
            errors.append('Description field is empty.')

        if errors:
            return render(request, 'notes/edit.html', {
                'note': note,
                'errors': errors
            })

        # Update note
        note.title = title
        note.description = description
        note.save()
        messages.success(request, 'Data updated successfully!')
        return redirect('notes:index')

    return render(request, 'notes/edit.html', {'note': note})


# DELETE - Delete note (equivalent to deleteAction.php)
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    messages.success(request, 'Note deleted successfully!')
    return redirect('notes:index')
