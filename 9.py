# Creating an empty list to store city names
cities = []

# Asking the user to enter city names
while True:
    city = input("Enter a city name (or 'quit' to exit): ")
    if city == "quit":
        break
    else:
        cities.append(city)

# Printing the list of city names
print("City names:", cities)

