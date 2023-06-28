#python 3.8 rasa 3.6

FROM python:3.8.16-slim

RUN python -m pip install rasa==3.5.11

WORKDIR /app
COPY . .

#RUN rasa init --no-prompt
#RUN rasa train nlu

#USER 1001

ENTRYPOINT ["rasa"]

CMD [ "run", "--enable-api", "--port", "8080" ]