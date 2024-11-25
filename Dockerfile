FROM debian:12
WORKDIR /usr/local/app

# Install python
RUN apt-get update && apt-get install -y python3

# Copy files
COPY src ./src
COPY --chmod=755 entrypoint.sh /entrypoint.sh

# Create delete dir
RUN mkdir /delete

# Run cron on startup
ENTRYPOINT ["/entrypoint.sh"]