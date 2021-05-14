FROM python:3.9

WORKDIR /usr/src/admin

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD sh -c "python manage.py migrate && gunicorn -w 3 -b 0.0.0.0:8000 admin.wsgi"