FROM python:3.8

# Install any necessary dependencies for your FS code
# For example, if you are using Python and need Flask:
RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \

RUN pip3 install flask
RUN pip3 install socket
# Copy your FS code into the container
COPY FS.py /dcn_app/FS.py

# Expose the port for HTTP communication (9090)
EXPOSE 9090

# Set the working directory
WORKDIR /dcn_app

# Run the FS code when the container starts
CMD ["python3", "FS.py"]
