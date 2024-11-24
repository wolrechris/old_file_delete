FROM python:3.12
WORKDIR /usr/local/app

# Copy in the source code
COPY src ./src

# Setup an app user so the container doesn't run as the root user
RUN useradd app
USER app

# Install cronjob in crontab & create cron log
COPY old-file-delete-cron /etc/cron.d/old-file-delete-cron
RUN chmod 0644 /etc/cron.d/old-file-delete-cron
RUN crontab /etc/cron.d/old-file-delete-cron
RUN touch /var/log/cron.log

# Run cron on startup
CMD cron && tail -f /var/log/cron.log