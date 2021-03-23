from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/jobs.db")
    surnames = ['Scott', 'Green', 'Brown']
    names = ['Ridley', 'Joshua', 'Ted']
    ages = ['21', '25', '30']
    positions = ['captain', 'navigator', 'captain assistant']
    specialities = ['research engineer', 'doctor', 'research engineer']
    addresses = ['module_1', 'module_1', 'module_2']
    emails = ['scott_chief@mars.org', 'green_sous_chef@mars.org', 'brown_navigator@mars.org']
    db_sess = db_session.create_session()
    for i in range(3):
        user = User()
        user.surname = surnames[i]
        user.name = names[i]
        user.age = ages[i]
        user.position = positions[i]
        user.speciality = specialities[i]
        user.address = addresses[i]
        user.email = emails[i]
        db_sess.add(user)
        db_sess.commit()


if __name__ == '__main__':
    main()
