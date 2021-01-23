FROM python:3.8

# Copy local code to container.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install -r requirements.txt

# Run web server on startup.
CMD gunicorn --bind .$PORT wsgi:app