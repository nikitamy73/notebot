import sqlite3
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "СЮДА_ВСТАВЬ_ТОКЕН_ОТ_BOTFATHER"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- База данных ---
def init_db():
    conn = sqlite3.connect("notes.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_note(user_id: int, text: str):
    conn = sqlite3.connect("notes.db")
    conn.execute("INSERT INTO notes (user_id, text) VALUES (?, ?)", (user_id, text))
    conn.commit()
    conn.close()

def get_notes(user_id: int):
    conn = sqlite3.connect("notes.db")
    rows = conn.execute("SELECT id, text FROM notes WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()
    return rows

def delete_note(note_id: int, user_id: int):
    conn = sqlite3.connect("notes.db")
    conn.execute("DELETE FROM notes WHERE id = ? AND user_id = ?", (note_id, user_id))
    conn.commit()
    conn.close()

# --- Хендлеры ---
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Я бот для заметок.\n\n"
        "/add текст — добавить\n"
        "/list — показать все\n"
        "/delete номер — удалить"
    )

@dp.message(Command("add"))
async def add(message: types.Message):
    text = message.text.replace("/add", "").strip()
    if not text:
        await message.answer("Напиши текст после /add")
        return
    add_note(message.from_user.id, text)
    await message.answer(f"✅ Заметка добавлена: {text}")

@dp.message(Command("list"))
async def list_notes(message: types.Message):
    notes = get_notes(message.from_user.id)
    if not notes:
        await message.answer("Заметок пока нет.")
        return
    text = "\n".join(f"{nid}. {t}" for nid, t in notes)
    await message.answer(f"📝 Твои заметки:\n\n{text}")

@dp.message(Command("delete"))
async def delete(message: types.Message):
    try:
        note_id = int(message.text.split()[1])
    except (IndexError, ValueError):
        await message.answer("Используй: /delete 3")
        return
    delete_note(note_id, message.from_user.id)
    await message.answer(f"🗑 Заметка {note_id} удалена")

# --- Запуск ---
async def main():
    init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())