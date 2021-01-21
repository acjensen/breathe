FROM python:3.7

# Copy local code to container.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .

# Install production dependencies.
RUN pip install Flask gunicorn

# Run web server on startup.
CMD exec gunicorn --bind .$PORT