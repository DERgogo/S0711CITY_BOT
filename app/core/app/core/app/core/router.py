from app.handlers.start import start_handler
from app.handlers.menu import menu_handler
from app.handlers.admin import admin_handler
from app.handlers.language import language_handler

def register_handlers(app):
    app.add_handler(start_handler)
    app.add_handler(menu_handler)
    app.add_handler(admin_handler)
    app.add_handler(language_handler)
