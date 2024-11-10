#!/bin/sh
# Wait until Redis server is ready
until redis-cli -h localhost ping; do
    echo "Waiting for Redis to start..."
    sleep 1
done

# Force reload initial data into Redis
echo "Reloading initial data..."
redis-cli -h localhost SET sample_data "$(cat /data/data.json)"
echo "Data reloaded."
