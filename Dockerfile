FROM ubuntu:20.04
RUN apt update && apt upgrade -y && apt install python3-flask python3-pip -y
RUN pip install Flask-Bootstrap4
RUN pip install Flask-WTF
COPY okurka.* /tmp/
COPY templates /tmp/templates
WORKDIR /tmp
ENV FLASK_APP="okurka" 
CMD ["flask", "run", "--host=0.0.0.0"]
