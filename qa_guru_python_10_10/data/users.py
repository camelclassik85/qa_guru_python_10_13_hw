from dataclasses import dataclass
import datetime
from enum import Enum


date = datetime.date(1955, 7, 20)


class Hobbies(Enum):
    Sports = 'Sports'
    Reading = 'Reading'
    Music = 'Music'


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_year: int
    birth_month: int
    birth_day: int
    subjects: list
    hobbies: list
    picture: str
    current_address: str
    state: str
    city: str


ad = User(
    first_name='Good',
    last_name='Game',
    email='gg@goga.com',
    gender="Male",
    phone_number="9876543210",
    birth_year=date.year,
    birth_month=date.month,
    birth_day=date.day,
    subjects=['Computer Science', 'English'],
    hobbies=[Hobbies.Sports.value, Hobbies.Music.value],
    picture="cat.jpg",
    current_address="Good for good 123456",
    state="Haryana",
    city="Karnal",
)
