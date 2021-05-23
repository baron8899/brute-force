import phonenumbers
from phonenumbers import geocoder
ch_number = phonenumbers.parse("+84973575238","CH")
geocoder.description_for_number(ch_number,"en")
