FROM python:3.6.2-stretch


RUN DEBIAN_FRONTEND=noninteractive \
  && apt-get update \
  && apt-get install -y voikko-fi python3-libvoikko

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt \
  && ln -s /usr/lib/python3/dist-packages/libvoikko.py libvoikko.py

COPY app.py ./

# ENTRYPOINT ["gunicorn", "app:app", "--bind=0.0.0.0:8000"]
ENTRYPOINT python3 app.py

EXPOSE 8000
