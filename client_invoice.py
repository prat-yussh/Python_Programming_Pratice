# Q1: Delivery Location Record

# A delivery location is stored as a tuple because its values should remain fixed:


# Do exactly this:

# Print the city using indexing.
# Print the latitude using indexing.
# Print the longitude using negative indexing.
# Unpack the tuple into:
# city, latitude, longitude
# Print all three unpacked variables.
# Print the tuple’s length.
# Print its data type.

# Use only indexing, unpacking, len() and type().

# Tuples preserve order and support indexing like lists, but tuples are immutable.

location = ("Bhubaneswar", 20.2961, 85.8245)

print("City:", location[0])
print("Latitude:", location[1])
print("Longitude:", location[-1])

city, latitude, longitude = location

print(city)
print(latitude)
print(longitude)

print("Length:", len(location))
print("Type:", type(location))