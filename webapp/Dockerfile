FROM python:3.10-alpine
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD webapp.py /var/server/app.py
CMD python /var/server/app.py
