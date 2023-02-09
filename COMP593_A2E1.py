"""
=================================================

 _____ ________  _________   _____  _____  _____ 
/  __ \  _  |  \/  || ___ \ |  ___||  _  ||____ |
| /  \/ | | | .  . || |_/ / |___ \ | |_| |    / /
| |   | | | | |\/| ||  __/      \ \\____ |    \ \
| \__/\ \_/ / |  | || |     /\__/ /.___/ /.___/ /
 \____/\___/\_|  |_/\_|     \____/ \____/ \____/ 
                                                 
=================================================

Assignment 2 - Exercise 1

Description:
 Creates a complex data structure and manipulates it then prints it out

Usage:
 python COMP593_A2E1.py
"""

def main():

    # Create a complex data structure
    about_me = {
        'full_name' : 'Shawn Kuzma',
        'student_id' : 10298214,
        'pizza_toppings' : [
            'PEPPERONI',
            'ANCHOVIES',
            'MUSHROOMS'
        ],
        'movies' :[
            {
                'title' : 'the thing',
                'genre' : 'sci-fi'
            },
            {
                'title' : 'conan the barbarian',
                'genre' : 'fantasy'
            }
        ]
    }

    # Add another movie to the data structure
    new_movie = {
        'title' : 'police story',
        'genre' : 'action'
    }
    about_me['movies'].append(new_movie)

    print_student_name_and_id(about_me)

    print_pizza_toppings(about_me)
    add_pizza_toppings(about_me, ('GREEN PEPPER', 'BACON'))
    print_pizza_toppings(about_me)

    print_movie_genres(about_me)
    
    print_movie_titles(about_me['movies'])
    
# Function that prints student name and ID	
def print_student_name_and_id(about_me):
    full_name = about_me['full_name']
    student_id = about_me['student_id']
    first_name = about_me['full_name'].split()[0]
    print(f'My name is {full_name}, but you can call me Sir {first_name}.')
    print(f'My student ID is {student_id}.')
    
# Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['pizza_toppings'].extend(toppings)
    about_me['pizza_toppings'].sort()
    for i,p in enumerate(about_me['pizza_toppings']):
        about_me['pizza_toppings'][i] = p.lower()

# Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print(f'\nMy favourite pizza toppings are:')
    for p in about_me['pizza_toppings']:
        print(f'- {p}')

# Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    mov_genres = [m['genre'] for m in about_me['movies']]
    if len(mov_genres) > 1:
        mov_genres[-1] = "and " + mov_genres[-1]
    genre_list = ', '.join(mov_genres)
    print(f"\nI like to watch {genre_list} movies.")

# Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    mov_titles = [m['title'].title() for m in movie_list]
    if len(mov_titles) > 1:
        mov_titles[-1] = "and " + mov_titles[-1]
    mov_list = ', '.join(mov_titles)
    print(f"\nSome of my favourite movies are {mov_list}!")
    
if __name__ == '__main__':
    main()