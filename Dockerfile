FROM python:3.11

WORKDIR /app

COPY . .

ENV TZ=America/Sao_Paulo

ENV MONGO_HOST='@devgrid.zr3ivam.mongodb.net/'
ENV MONGO_PASSWORD='app741852'
ENV MONGO_USERNAME='aplicativo'
ENV DATABASE_ENVIROMENT='adm'
ENV API_key='1a89dbd68d7f3e8e25034127f223f9ba'

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]