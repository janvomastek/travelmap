# import pygal library
import pygal
# create a world map
worldmap = pygal.maps.world.World()
# set the title of the map
worldmap.title = 'Countries'

def add_list_of_places_with_year_as_title(list_of_places, year):
    # set the title of the map
    worldmap.title = 'Countries'

    # adding the countries
    worldmap.add(year, list_of_places)


def generate_wordlmap():
    # save into the file
    worldmap.render_to_file('abc.svg')

    print("Success")

