# 📝 Django Mini‑Project: Notes

Простой учебный проект на **Django**, демонстрирующий маршруты и View‑функции.

## 🚀 Функции
- Главная страница приложения
- Список всех заметок
- Фильтр заметок по категории
- Детальная страница заметки

## ⚡ Запуск
```bash
git clone https://github.com/Andasbek/notebook_project.git
cd notebook_project
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
pip install django
python manage.py runserver
🌐 Основные маршруты
/notes/ — главная

/notes/all/ — все заметки

/notes/category/<category>/ — по категории

/notes/note/<note_id>/ — детальная заметка
