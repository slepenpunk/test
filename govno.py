# Create 5 cats with different specifications of color, mood and age.
import random
class Cats():
    """Create different cats"""
    total = 0
    @staticmethod
    def total_cats():
        print('total cats:', Cats.total)
    def __init__(self, color, mood, age):
        self.color = color
        self.mood = mood
        self.age = age
        Cats.total += 1

    def __str__(self):
        rep = (f'Create a new cat!\n'
               f'Color - {self.color}\n'
               f'Mood - {self.mood}\n'
               f'Age - {self.age}\n')
        return rep


def random_color(color):
    color1 = random.choice(color)
    return color1


def random_mood(mood):
    mood1 = random.choice(mood)
    return mood1


def random_age():
    age1 = random.randint(1, 20)
    return age1


def main():
    colors = ('White', 'Black', 'Gray', 'Brown')
    moods = ('Good', 'Bad', 'Very Good', 'Very bad')

    color1 = random_color(colors)
    mood1 = random_mood(moods)
    age1 = random_age()


    color2 = random_color(colors)
    mood2 = random_mood(moods)
    age2 = random_age()

    color3 = random_color(colors)
    mood3 = random_mood(moods)
    age3 = random_age()

    color4 = random_color(colors)
    mood4 = random_mood(moods)
    age4 = random_age()

    color5 = random_color(colors)
    mood5 = random_mood(moods)
    age5 = random_age()

    cat1 = Cats(color1, mood1, age1)
    cat2 = Cats(color2, mood2, age2)
    cat3 = Cats(color3, mood3, age3)
    cat4 = Cats(color4, mood4, age4)
    cat5 = Cats(color5, mood5, age5)

    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    print(cat5)

    Cats.total_cats()

main()