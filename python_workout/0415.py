print('Chapter 04 - Exercise 15')
print('')
CITIES_RAINFALL = {}


def get_rainfall():
    """
        Tracks rainrall in a number of cities.

        _Users of your program will enter the name of a 
        city; if the city name is blank, then the function 
        prints a report .. 
        Then the program should also ask the user 
        how much rain has fallen in that city 
        (typically measured in millimeters)._
    """
    while True:
        city = input('City: ')
        try:
            if city == '':
                raise ValueError
            amount_rained = input(f'How much (mm) did it rain in {city}?: ')
            CITIES_RAINFALL[city.strip()] = amount_rained
        except ValueError:
            print('Goodbye. Here is your report')
            template = "{0:10} {1:10}"
            for city_to_value in CITIES_RAINFALL.items():
                formatted = template.format(*city_to_value)
                print(formatted)
            break


if __name__ == '__main__':
    get_rainfall()
