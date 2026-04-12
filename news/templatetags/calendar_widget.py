import calendar
from datetime import date

from django import template

from ..calendar_i18n import MONTHS, WEEKDAYS_SHORT, calendar_lang

register = template.Library()


@register.filter
def dict_key(d, key):
    return d.get(key, [])


@register.simple_tag
def format_date_ymd(year, month, day):
    return f"{year}-{int(month):02d}-{int(day):02d}"


@register.inclusion_tag('widgets/calendar.html')
def render_calendar(year=None, month=None, events_by_day=dict):
    today = date.today()
    lang = calendar_lang()
    months = MONTHS[lang]
    weekdays = WEEKDAYS_SHORT[lang]

    if month == 1:
        prev_month, prev_year = 12, year - 1
    else:
        prev_month, prev_year = month - 1, year

    if month == 12:
        next_month, next_year = 1, year + 1
    else:
        next_month, next_year = month + 1, year

    month_name = months[month]
    month_days = calendar.monthcalendar(year, month)

    return {
        'month': month,
        'year': year,
        'month_days': month_days,
        'title': f"{month_name.capitalize()} {year}",
        'weekdays': weekdays,
        'today': today,
        'prev_year': prev_year,
        'prev_month': prev_month,
        'next_year': next_year,
        'next_month': next_month,
        'events_by_day': events_by_day,
    }
