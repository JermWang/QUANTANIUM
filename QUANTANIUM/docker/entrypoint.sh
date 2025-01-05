#!/bin/bash
# Entrypoint script for initializing the application

# Migrate database if necessary
echo "Initializing application..."
exec "$@"