FROM debian:12
WORKDIR /usr/local/app

# Install python
RUN apt-get update && apt-get install -y python3 cron

# Copy in the source code
COPY src ./src
COPY --chmod=755 entrypoint.sh /entrypoint.sh

# Install cronjob in crontab & create cron log
COPY old-file-delete-cron /etc/cron.d/old-file-delete-cron
RUN chmod 0644 /etc/cron.d/old-file-delete-cron
RUN crontab /etc/cron.d/old-file-delete-cron
RUN touch /var/log/cron.log

# Create delete dir
RUN mkdir /delete

# Run cron on startup
ENTRYPOINT ["/entrypoint.sh"]