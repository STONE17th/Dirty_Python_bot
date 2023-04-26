from loader import settings_db, PICTURES


def load_settings():
    data = settings_db.load(type_set='poster')
    PICTURES.update({item[1]: item[3] for item in data})


def save_posters(data: dict[str, str]):
    PICTURES.update(data)
    settings_db.save_settings(PICTURES, 'poster')
