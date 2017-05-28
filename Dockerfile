FROM python:3.6.1

# See https://hub.docker.com/_/python/ for more info on the base image

LABEL maintainer="Stuart Whitehead"
LABEL name="api.stuart.is"
LABEL description="Development and testing container"

WORKDIR /usr/src/application
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

ENTRYPOINT ["bin/entrypoint.sh"]
CMD ["start"]
EXPOSE 8000
