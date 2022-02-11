FROM python:3.7

WORKDIR /netflix_code

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
