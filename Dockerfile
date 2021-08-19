FROM nginx:latest
COPY nginx.log .
COPY Carta.py .
RUN apt-get update && apt-get install -y \
    python-pip
RUN pip install Flask
ENTRYPOINT [ "python", "Carta.py" ]
