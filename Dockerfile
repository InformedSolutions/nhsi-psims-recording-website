FROM python:3.5-slim
ENV PYTHONUNBUFFERED 1
ARG PROJECT_SETTINGS

RUN mkdir /source
WORKDIR /source
ADD . /source/
RUN pip install -r requirements.txt
RUN chmod +x /source/docker-entrypoint.sh
EXPOSE 8000
CMD ["/source/docker-entrypoint.sh"]
