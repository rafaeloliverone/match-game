FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/

RUN pip install --upgrade pip --no-cache-dir
RUN pip install -r requirements.txt --no-cache-dir

COPY . /code/
COPY ./entrypoint.sh /code/
RUN chmod +x ./entrypoint.sh