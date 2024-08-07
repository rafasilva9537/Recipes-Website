from faker import Faker
from random import randint
from pprint import pprint
fake = Faker()

def create_fake_recipe():
    fake_recipe: dict = {
        'title': fake.sentence(nb_words=4),
        'ingredients': [ fake.sentence(nb_words=3) for _ in range(randint(3, 12)) ],
        'steps': [ fake.sentence(nb_words=15, variable_nb_words= True) for _ in range(0, randint(3, 9))],
        'cook_time': randint(20, 220),
        'cook_time_unit': 'Minutes',
        'servings': randint(1, 10), 
        'creation_date_time': fake.date_time(),
        'author': {
            'first_name': fake.first_name(),
            'last_name': fake.last_name()
        },
        'category': fake.word(),
        'image': f'https://loremflickr.com/{randint(1000,1280)}/{720}/recipe,food'
    }

    return fake_recipe

if __name__ == '__main__':
    pprint(create_fake_recipe(), sort_dicts=False)