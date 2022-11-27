#!/usr/bin/python3
""" module for place class """


class Place(BaseModel):
    """ place class attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = ""
    number_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = ""
