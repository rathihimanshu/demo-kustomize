FROM redis:alpine
COPY data.json /data/data.json
COPY init_data.sh /init_data.sh
RUN chmod +x /init_data.sh
CMD ["sh", "-c", "redis-server & sleep 5 && sh /init_data.sh && tail -f /dev/null"]
