FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

Run git clone https://github.com/metacomp/nyu-cs2262-001-fa20.git

# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask
RUN pip install datetime

USER nyu

COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
