from libs.publisher_api import run_query
from datetime import date

# Example request for direct sell data from Sharethrough Publisher API
# Set this request body according to your needs
# API docs: https://support.sharethrough.com/hc/en-us/articles/360044449471-Sharethrough-Publisher-API-Documentation
request_body = {
    "startDate": date.today().strftime("%Y-%m-%d"),
    "endDate": date.today().strftime("%Y-%m-%d"),
    "groupBy": ["date", "supply_name"],
    "filterBy": [
        {
            "operator": "EQUALS",
            "field": "device_type",
            "value": "Smartphone"
        },
        {
            "operator": "EQUALS",
            "field": "creative_type",
            "value": "clickout"
        }
    ],
    "fields": ["pub_earnings", "rendered_impressions"],
}

# set this to True if you want your results as plain json instead of CSV
json = False


def request_programmatic():
    run_query('programmatic', request_body, json)


if __name__ == '__main__':
    request_programmatic()
