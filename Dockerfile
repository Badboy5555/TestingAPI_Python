FROM python:3.11.2

LABEL QA_level='API_tests'

WORKDIR /usr/src/api_tests

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /tests .

VOLUME /usr/src/api_tests/test_results

ENV api_version=v1

CMD python -m pytest tests --alluredir=test_results