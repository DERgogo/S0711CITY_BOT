import datetime

LANG = "de"

def set_language(l):
    global LANG
    LANG = l

def get_welcome_message():
    hour = datetime.datetime.now().hour

    if hour < 12:
        t = "Guten Morgen Boss. Wir bauen wieder Zukunft."
    elif hour < 18:
        t = "Halbzeit. Vision 200%. Weiter geht’s."
    else:
        t = "Stuttgart wird dunkel, aber dein Grind läuft."

    ascii = """
██████╗ ██╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██║   ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██████╔╝██║   ██║   ██║   ██║   ██║██████╔╝█████╗  
██╔═══╝ ██║   ██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██║     ╚██████╔╝   ██║   ╚██████╔╝██║  ██║███████╗
╚═╝      ╚═════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
    """

    translations = {
        "de": t,
        "en": "Future mode on. Let's move.",
        "hr": "Brate, vrijeme je za rad. Ajmo."
    }

    return ascii + "\n\n" + translations.get(LANG, t)
