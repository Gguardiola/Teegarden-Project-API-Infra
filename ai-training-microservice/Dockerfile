FROM python:3.9

WORKDIR /code

ENV API_SECRET="teegarden-tfg-2025"
ENV env="tst"
ENV MINIO_SECRET_KEY="minioadmin"
ENV MINIO_ACCESS_KEY="minioadmin"

RUN apt-get update && apt-get install -y git nano cron

RUN git clone https://github.com/Gguardiola/Teegarden-Project-Intellicombat-RL-Trainer.git /code/app

RUN touch /code/app/intellicombat_training_logs_manager/__init__.py \
 && touch /code/app/intellicombat_training_logs_manager/engine/__init__.py

COPY ./app /code/app

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN chmod +x /code/app/intellicombat_rl_trainer/trainer.sh

RUN echo "0 3 * * * /bin/bash /code/app/intellicombat_rl_trainer/trainer.sh >> /var/log/cron.log 2>&1" > /etc/cron.d/trainer-cron \
 && chmod 0644 /etc/cron.d/trainer-cron \
 && crontab /etc/cron.d/trainer-cron

# ENTRYPOINT
COPY entrypoint.sh /code/entrypoint.sh
RUN chmod +x /code/entrypoint.sh

CMD ["/code/entrypoint.sh"]