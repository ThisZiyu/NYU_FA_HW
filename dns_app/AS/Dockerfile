FROM python:3.8

# Install any necessary dependencies for your AS code
# For example, if you are using Python and need the socket library:
RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install flask

# Copy your AS code into the container
COPY AS.py /dcn_app/AS.py

# Expose the port for DNS communication (53533)
EXPOSE 53533/udp

# Set the working directory
WORKDIR /dcn_app

# Run the AS code when the container starts
CMD ["python3", "AS.py"]
