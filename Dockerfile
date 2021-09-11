ARG VARIANT=3.8-slim
ARG APP_PORT=8083 
FROM python:${VARIANT}


RUN pip install pipenv

COPY requirements.txt /lib

RUN  pip install -r /lib/requirements.txt

COPY Pipfile.lock /tmp/Pipfile.lock
COPY Pipfile /tmp/Pipfile

WORKDIR /tmp
RUN pipenv install --system

RUN adduser --disabled-password worker
USER worker
WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin/${PATH}"
ENV PYTHONPATH="$PYTHONPATH"
ENV APP_PORT 8083

COPY main.py /home/worker/

COPY --chown=worker:worker . .

WORKDIR /home/worker


EXPOSE 8083

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8083"]