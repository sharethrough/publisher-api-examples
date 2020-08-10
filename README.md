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

Next, update `setup.py` such that the `AUTH_TOKEN` variable matches your authentication token for the Publisher API.

## How to use

There are two report types: programmatic and direct sell.
 
The `run_programmatic.py` and `run_direct_sell.py` files contain the basic logic for sending requests to the publisher API for each report type.

Every request to the Publisher API must consist of a request body. There is an example request body for each report type inside its relevant python script, which you can edit according to your needs. To help you, you can refer to the [documentation](https://support.sharethrough.com/hc/en-us/articles/360044449471-Sharethrough-Publisher-API-Documentation) for the exact specification.

Once you have set up your request, you need to decide if you want results in CSV format or JSON. By default this script will output results in CSV. You can instead have results in JSON format by setting the `json` variable to `True` inside the script.

When you run the script, it will write to a file in the `results/` directory named
```bash
<current_date>-<current_time>.<report_type>.<format>
# examples
20200810-131101.direct-sell.csv
20200809-162319.programmatic.json
```
If there is no `results/` directory in place, it will be created for you.
