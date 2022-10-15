# Create 5 cats with different specifications of color and mood.
import random
class Cats():
    """Create different cats"""
    total = 0
    @staticmethod
    def total_cats():
        print('total cats:', Cats.total)
    def __init__(self, color, mood):
        self.color = color
        self.mood = mood
        Cats.total += 1

    def __str__(self):
        rep = (f'Create a new cat!\n'
               f'Color - {self.color}\n'
               f'Mood - {self.mood}\n')
        return rep


def random_color(color):
    color1 = random.choice(color)
    return color1


def random_mood(mood):
    mood1 = random.choice(mood)
    return mood1

def main():
    colors = ('White', 'Black', 'Gray', 'Brown')
    moods = ('Good', 'Bad', 'Very Good', 'Very bad')

    color1 = random_color(colors)
    mood1 = random_mood(moods)

    color2 = random_color(colors)
    mood2 = random_mood(moods)

    color3 = random_color(colors)
    mood3 = random_mood(moods)

    color4 = random_color(colors)
    mood4 = random_mood(moods)

    color5 = random_color(colors)
    mood5 = random_mood(moods)

    cat1 = Cats(color1, mood1)
    cat2 = Cats(color2, mood2)
    cat3 = Cats(color3, mood3)
    cat4 = Cats(color4, mood4)
    cat5 = Cats(color5, mood5)

    print(cat1)
    print(cat2)
    print(cat3)
    print(cat4)
    print(cat5)

    Cats.total_cats()

main()