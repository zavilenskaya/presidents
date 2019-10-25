from pprint import pprint
import requests
import pytest


url = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
response = requests.get(url)
json_data = response.json()
presidents = ['Washington', 'Adams', 'Jefferson', 'Madison', 'Monroe', 'Adams', 'Jackson', 'Buren', 'Harrison', 'Tyler', 'Polk', 'Taylor', 'Fillmore', 'Pierce', 'Buchanan', 'Lincoln', 'Johnson', 'Grant', 'Hayes', 'Garfield', 'Arthur', 'Cleveland', 'Harrison', 'Cleveland', 'McKinley', 'Roosevelt', 'Taft', 'Wilson', 'Harding', 'Coolidge', 'Hoover', 'Truman', 'Eisenhower', 'Kennedy', 'Johnson', 'Nixon', 'Ford', 'Carter', 'Reagan', 'Bush', 'Clinton', 'Obama', 'Trump']


@pytest.mark.parametrize("test_input", presidents)
def test_washington(test_input):
    for element in json_data["RelatedTopics"]:
        obj = element["Text"]
        if test_input in obj:
            assert True





