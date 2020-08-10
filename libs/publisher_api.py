import requests
from datetime import datetime
from setup import PUB_API_URL, AUTH_TOKEN
from libs.auth import BearerAuth


def run_query(report_type, request_body, json=False):
    url = f"{PUB_API_URL}/{report_type}"
    # comment below line if you want plain json instead
    headers = {} if json is True else {'accept': 'text/csv'}
    r = requests.post(url, json=request_body, headers=headers, auth=BearerAuth(AUTH_TOKEN))

    if r.status_code == 200:
        response_data = r.json() if json is True else r.text
        return write_result(report_type, response_data, json)
    else:
        print("Request to publisher API was not successful, see response below")
        print(r.json())
        exit(1)


def write_result(report_type, data, json=False):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_type = "json" if json is True else "csv"
    filename = f"results/{timestamp}.{report_type}.{file_type}"

    f = open(filename, "w+")
    f.write(data)
    f.close()
