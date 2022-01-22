"""Program should have the ability to replace any instance of a parent class
with an instance of one of its child classes without negative side affects
"""

from datetime import date
from typing import List, Dict


class User:
    settings: Dict = None

    def __init__(self, email):
        self.email = email


class AdminUser(User):
    settings: List = None


def signed_in_today(users: List[User]):
    for user in users:
        if user.settings['signed_in'] == date.today():
            print(f"{user.email} signed in today")


if __name__ == '__main__':
    user = User(email='user@test.com')
    user.settings = {'level': 'Low Security', 'status': 'Live', 'signed_in': date.today()}

    admin = AdminUser(email='admin@test.com')
    admin.settings = ['Editor', 'VIP', date.today()]
    signed_in_today([user, admin])