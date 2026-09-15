from bot import add_note, get_notes, delete_note, init_db

def setup_function():
    init_db()

def test_add_and_get():
    add_note(1, "купить хлеб")
    notes = get_notes(1)
    assert len(notes) >= 1
    assert notes[-1][1] == "купить хлеб"

def test_delete():
    add_note(2, "удалить меня")
    note_id = get_notes(2)[-1][0]
    delete_note(note_id, 2)
    assert all(n[0] != note_id for n in get_notes(2))

def test_empty():
    assert get_notes(999) == []