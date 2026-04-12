"""Localized month/weekday labels for calendar UI (widgets + views)."""
from datetime import date

from django.utils import translation

MONTHS = {
    'ru': {
        1: 'январь',
        2: 'февраль',
        3: 'март',
        4: 'апрель',
        5: 'май',
        6: 'июнь',
        7: 'июль',
        8: 'август',
        9: 'сентябрь',
        10: 'октябрь',
        11: 'ноябрь',
        12: 'декабрь',
    },
    'en': {
        1: 'january',
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december',
    },
    'kz': {
        1: 'қаңтар',
        2: 'ақпан',
        3: 'наурыз',
        4: 'сәуір',
        5: 'мамыр',
        6: 'маусым',
        7: 'шілде',
        8: 'тамыз',
        9: 'қыркүйек',
        10: 'қазан',
        11: 'қараша',
        12: 'желтоқсан',
    },
}

WEEKDAYS_SHORT = {
    'ru': ['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'],
    'en': ['mo', 'tu', 'we', 'th', 'fr', 'sa', 'su'],
    'kz': ['дс', 'сс', 'ср', 'бс', 'жм', 'сн', 'жк'],
}


def calendar_lang():
    lang = translation.get_language() or 'ru'
    if lang.startswith('en'):
        return 'en'
    if lang.startswith('kz'):
        return 'kz'
    return 'ru'


def month_names_capitalized():
    """Labels for <select> on event calendar (current UI language)."""
    lang = calendar_lang()
    return [MONTHS[lang][i].capitalize() for i in range(1, 13)]


def month_get_param_to_number(label):
    """Resolve ?month= from GET (any supported language spelling)."""
    if not label or not str(label).strip():
        return None
    normalized = str(label).strip().lower()
    for _lang, months in MONTHS.items():
        for num, name in months.items():
            if name.lower() == normalized:
                return num
    return None


def format_calendar_day_heading(d: date) -> str:
    """e.g. '12 April 2026' / '12 апреля' style — day + month name in active language."""
    lang = calendar_lang()
    return f"{d.day} {MONTHS[lang][d.month].capitalize()}"
