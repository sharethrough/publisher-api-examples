# publisher-api-examples
Example requests for Sharethrough Publisher API

## Installation

You will need
- Python 3.8
- pipenv

Install with
```bash
pipenv install
```

## How to use

Update `setup.py` such that the `AUTH_TOKEN` variable matches your authentication token for the Publisher API.

The `run_direct_sell.py` and `run_programmatic.py` files contain the basic logic for sending requests to the publisher API.

These scripts are set up to query the publisher API using the request body that you define and will print the results to a file in the `results/` directory. The file name will be the current date/time and the report type (`direct-sell` or `programmatic`, depending on which script you triggered).

Here you can set your request body which will determine what fields you are requesting and how your want your data grouped and sliced. For help building the correct request body for your needs, refer to the [documentation](https://support.sharethrough.com/hc/en-us/articles/360044449471-Sharethrough-Publisher-API-Documentation).

By default the scripts in this git repository will return results in CSV format. It is possible to instead have results in JSON format by setting the `json` variable to `True`.
