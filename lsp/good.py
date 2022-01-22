"""Program should have the ability to replace any instance of a parent class
with an instance of one of its child classes without negative side affects
"""
import dataclasses
from datetime import date
from typing import List, Dict


@dataclasses.dataclass
class Settings:
    level: str
    status: str
    signed_in: date


class User:
    _settings: Settings

    def __init__(self, email):
        self.email = email

    def set_settings(self, level, status, signed_in):
        self._settings = Settings(
            level=level,
            status=status,
            signed_in=signed_in,
        )

    def get_settings(self) -> Settings:
        return self._settings


class AdminUser(User):
    pass


def signed_in_today(users: List[User]):
    for user in users:
        if user.get_settings().signed_in == date.today():
            print(f"{user.email} signed in today")


if __name__ == '__main__':
    user = User(email='user@test.com')
    user.set_settings(
        level='Low Security',
        status='Live',
        signed_in=date.today(),
    )

    admin = AdminUser(email='admin@test.com')
    admin.set_settings(
        level='Editor',
        status='VIP',
        signed_in=date.today(),
    )
    signed_in_today([user, admin])