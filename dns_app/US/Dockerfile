FROM python:3.8

# Install any necessary dependencies for your US code
# For example, if you are using Python and need Flask:
RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

RUN pip3 install flask
RUN pip3 install requests
RUN pip3 install socket

RUN groupadd -g 799 nyu && \
    useradd -r -u 999 -g nyu nyu

USER nyu

COPY --chown=nyu:nyu .. .

# Copy your US code into the container
COPY US.py /dcn_app/US.py

# Expose the port for HTTP communication (8080)
EXPOSE 8080

# Set the working directory
WORKDIR /dcn_app

# Run the US code when the container starts
CMD ["python3", "US.py"]
