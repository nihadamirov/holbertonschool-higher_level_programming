# Start with the same Alpine base image
FROM alpine:3.15

# Install curl
RUN apk add --no-cache curl

# Copy the configuration file into the container
COPY config.txt /app/config.txt

# Command to run when the container starts
CMD ["sh"]