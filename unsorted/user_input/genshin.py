import calendar

FARM_MATERIALS = {
    'Freedom': {
        'domain': 'Frosted Altar',
        'characters': ["Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Childe", "Anemo MC"],
        'days': (calendar.MONDAY, calendar.THURSDAY)
    },
    'Prosperity': {
        'domain' : 'Domain of Mastery: Altar of Flames',
        'characters': ['Keqing','Ningguang','Qiqi','Shenhe', 'Xiao','Yelan'],
        'days': (calendar.MONDAY, calendar.THURSDAY)
    },
    'Transience':{
        'domain': 'Domain of Mastery: Reign of Violet',
        'characters': ['Electro MC','Kokomi','Shikanoin','Heizou','Thoma','Yoimiya'],
        'days': (calendar.MONDAY, calendar.THURSDAY)
    }




}


def get_farm_days(character: str) -> tuple:
    match character:
        case ["Aloy", "Amber", "Barbara", "Diona", "Klee", "Sucrose", "Childe", "Anemo MC"]:
            return calendar.MONDAY, calendar.THURSDAY
        case _:
            return None
