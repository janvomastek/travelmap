import csv
import mapplotter
list_of_places = []

with open('country_code.csv', 'r') as data:
  country_codes = list(csv.DictReader(data))
  #print(country_codes)

def search_country_code(country_name):
  for code in country_codes:
    if code['Country Name'] == country_name:
      return code['Country Code']
  return None

with open('when_place.csv', 'r') as data:
  country_list = list(csv.DictReader(data))
  for country in country_list:
    country['Country'] = search_country_code(country['Country'])
    if country['Country'] == None:
      print("Country not found: " + country['Country Name'])

# Count the number of times each place appears in the list for each year
# and put the results in a new dictionary
place_counts = {}
for country in country_list:
  if country['Year'] in place_counts:
    if country['Country'] in place_counts[country['Year']]:
      place_counts[country['Year']][country['Country']] += 1
    else:
      place_counts[country['Year']][country['Country']] = 1
  else:
    place_counts[country['Year']] = {}
    place_counts[country['Year']][country['Country']] = 1

#print(place_counts)





years=[]
for year in place_counts:
    years.append(year)
years.sort(reverse=True)
for year in years:
    mapplotter.add_list_of_places_with_year_as_title(place_counts[year], year)
  
mapplotter.generate_wordlmap()

''' 
  for line in csv.DictReader(data):
      for code in country_codes:
        if line['Country'] == code['Country Name']:
          #print(code['Country Code'])
          list_of_places.append(code['Country Code'])
          
# Count the number of times each place appears in the list
# and put the results in a new dictionary
place_counts = {}
for place in list_of_places:
  if place in place_counts:
    place_counts[place] += 1
  else:
    place_counts[place] = 1

# Print the place counts
#print(place_counts)

mapplotter.generate_wordlmap(place_counts)


'''