FROM python:3.8.16-slim

WORKDIR /app

COPY . .

RUN python -m pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "flask" ]

CMD [ "--app", "main.py", "--debug", "run" , "--host=0.0.0.0"]
