import requests


# Testing Heroku URL #
def request():
    request = requests.get('https://data-centric-dev.herokuapp.com/')
    print('Heroku server response for index page - {r}'.format(r=request))


request()

# To test MongoDB connection I have created a test database and a test config
