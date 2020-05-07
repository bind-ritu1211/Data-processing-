FORM python:3.6
COPY . /code
WORKON /code
RUN pip install -r /code/requirements.txt
RUN python App.py