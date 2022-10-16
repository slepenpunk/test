# Create cats with different specifications of color, mood and age.
import random


class Cats():
    """Create different cats"""
    total = 0
    colors = ['White', 'Black', 'Gray', 'Brown']
    moods = ('凸(￣ヘ￣)', '٩(ఠ益ఠ)۶', '(▽◕ ᴥ ◕▽)', '(´｡• ᵕ •｡)')

    @staticmethod
    def total_cats():
        print('Total cats:', Cats.total)

    @staticmethod
    def add_colors(color):
        new = Cats.colors.append(color)
        return new

    def __init__(self, color, mood, age):
        self.color = color
        self.mood = mood
        self.age = age
        Cats.total += 1

    def __str__(self):
        rep = (f'\nA new cat has been created!\n'
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
    colors = Cats.colors
    choice = None
    while choice != '0':
        print(
            '''
            0 - Exit
            1 - Create cats
            2 - View total cats
            3 - View the colors of cats
            4 - Add color
            5 - Delete color
            ''')
        choice = input('Enter your choice: ')
        if choice == '0':
            break
        elif choice == '1':
            c = int(input('Enter how many cats you want to create: '))
            if colors:
                for i in range(c):
                    color1 = random_color(Cats.colors)
                    mood1 = random_mood(Cats.moods)
                    age1 = random_age()
                    cat1 = Cats(color1, mood1, age1)
                    print(cat1)
            else:
                print('No colors!')
        elif choice == '2':
            Cats.total_cats()
        elif choice == '3':
            for i in colors:
                print(i)
        elif choice == '4':
            new_color = input('Enter color new color: ').capitalize()
            Cats.add_colors(new_color)
            print('Color', new_color, 'was been added!')
        elif choice == '5':
            delete_color = input('Enter color which you want delete: ').capitalize()
            if delete_color in colors:
                colors.remove(delete_color)
                print('Color', delete_color, 'was been deleted!')
            else:
                print('No such is color!')
        else:
            print('Unknown command!')


main()
