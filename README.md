

## Setup

*Pre-requisites:*
- Python 3.6+

### Required dependencies

To install Python dependencies, run the following commands:

```
python3 -m venv venv
. ./venv/bin/activate
pip install -r ./requirements.txt

(cd ./ticketing && python manage.py migrate)
(cd ./recommendations && python manage.py migrate)
```