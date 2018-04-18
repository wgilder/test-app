FROM python:3.7-rc-alpine

# Set the Flask work directory
WORKDIR /app
ADD . /app

# Install the reqs for the web app
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Port to deliver Flask results
EXPOSE 5000

ENV FLASK_APP=entrypoint.py

# Run the Flask app
CMD ["flask", "run", "--host=0.0.0.0"]

