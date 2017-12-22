from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """ Return 2 letters country code used by Pygal to a given country """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # if found no country, return None
    return None
