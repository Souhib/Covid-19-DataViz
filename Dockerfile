FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements-pip.txt
CMD python run.py
EXPOSE 5000