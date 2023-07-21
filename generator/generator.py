import os
import random

from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()


def generated_person():
    yield Person(
        full_name=f"{faker_ru.first_name()} {faker_ru.last_name()} {faker_ru.middle_name()}",
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        age=random.randint(18, 65),
        salary=random.randint(100000, 250000),
        department=faker_ru.job(),
        email=faker_ru.free_email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
        mobile=faker_ru.msisdn(),
        password=faker_en.password(),
    )


def generated_file():
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = f'filetest_{random.randint(1, 999)}.txt'
    file_path = os.path.join(current_dir, file_name)
    file = open(file_path, 'w+')
    file.write(f'Hello world {random.randint(1, 999)}')
    file.close()
    return file_name, file_path


def generated_file_base64_to_jpeg(base_str):
    current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    file_name = f'filetest_{random.randint(1, 999)}.jpeg'
    file_path = os.path.join(current_dir, file_name)
    file = open(file_path, 'wb+')
    file.write(base_str)
    check_file = os.path.exists(file_path)
    file.close()
    os.remove(file_path)
    return check_file


def random_item_subjects():
    data = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Accounting", "Commerce"]
    result_item = data[random.randint(0, 8)]
    return result_item


def random_item_color():
    data = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    result_item = data[random.randint(0, 8)]
    return result_item


def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )


def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time="12:00"
    )
