import requests, json

api_key = 'example_key' # find your key in Mixpanel settings

def get_mixpanel_data():
    import requests

    data = [
      ('from_date', '2016-02-11'),
      ('to_date', '2016-02-11'),
      ('event', 'Viewed Page'),
    ]

    requests('get', 'https://mixpanel.com/api/2.0/segmentation/', data=data, auth=(api_key))

get_mixpanel_data()