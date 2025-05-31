import re
from datetime import datetime, date

HONAPOK = [
    "január", "február", "március", "április", "május", "június",
    "július", "augusztus", "szeptember", "október", "november", "december"
]
NAP_MAP = {
    "egy": 1, "kettő": 2, "ketto": 2, "három": 3, "harom": 3, "négy": 4, "negy": 4,
    "öt": 5, "ot": 5, "hat": 6, "hét": 7, "het": 7, "nyolc": 8, "kilenc": 9, "tíz": 10, "tiz": 10,
    "tizenegy": 11, "tizenkettő": 12, "tizenketto": 12, "tizenhárom": 13, "tizenharom": 13,
    "tizennégy": 14, "tizennegy": 14, "tizenöt": 15, "tizenot": 15, "tizenhat": 16,
    "tizenhét": 17, "tizenhet": 17, "tizennyolc": 18, "tizenkilenc": 19, "húsz": 20, "husz": 20,
    "huszonegy":21,"huszonkettő":22,"huszonketto":22,"huszonhárom":23,"huszonharom":23,
    "huszonnégy":24,"huszonnegy":24,"huszonöt":25,"huszonot":25,"huszonhat":26,"huszonhét":27,"huszonhet":27,
    "huszonnyolc":28,"huszonkilenc":29,"harminc":30,"harmincegy":31
}

def parse_date(datestr):
    s = datestr.strip().lower()
    for sep in ['-', '.', '/', ' ']:
        try:
            dt = datetime.strptime(s, f"%Y{sep}%m{sep}%d")
            return dt.date()
        except Exception:
            pass
    match = re.match(r"(\d{4})\s*([a-záéíóöőúüű]+)\s*([\w\.]+)", s)
    if match:
        year = int(match.group(1))
        month_txt = match.group(2)
        day_txt = match.group(3).replace(".", "")
        try:
            month = HONAPOK.index(month_txt) + 1
        except ValueError:
            month = None
        try:
            day = int(day_txt)
        except ValueError:
            day = NAP_MAP.get(day_txt, None)
        if year and month and day:
            try:
                return date(year, month, day)
            except Exception:
                pass
    raise ValueError(f"Ismeretlen dátumformátum: {datestr}")

def normalize_flight_number(flight_number):
    return flight_number.strip().upper()