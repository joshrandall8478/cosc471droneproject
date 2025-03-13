# Use the official PHP image as the base image
FROM php:7.4-cli

# Set the working directory
WORKDIR /var/www/html

# Copy the current directory contents into the container
COPY assets /var/www/html/assets
COPY index.php /var/www/html
COPY styles.css /var/www/html

# Install necessary PHP extensions
RUN docker-php-ext-install mysqli

# Expose port 80 to the outside world
EXPOSE 80

# Run PHP built-in server
CMD ["php", "-S", "0.0.0.0:80", "-t", "/var/www/html"]