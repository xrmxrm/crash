from city_functions import format_city

def test_city_country_pop():
    formatted_city = format_city('santiago', 'chile', 5000000)
    assert formatted_city == 'Santiago, Chile -- population 5000000'

def test_city_country_no_pop():
    formatted_city = format_city('santiago', 'chile')
    assert formatted_city == 'Santiago, Chile'