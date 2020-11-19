
# This docker file is automatically created by NO-HEADACHE-DJANGO
# Please star me on github: http://github.com/mrsaemir/no-headache-django

# Base Python docker image:
FROM python:3.8

# These variables are required for Python:
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Database-related libraries:
RUN apt update && apt install -y libpq-dev

# Setting project's working directory:
WORKDIR /home/user/project_core
COPY . /home/user/project_core

# Static Files:
RUN mkdir -p /home/user/media
RUN mkdir -p /home/user/static

# Installing project requirement:
RUN pip install -r ./requirements.txt

# Setting right file permissions:
RUN chmod -R 777 /home/user
RUN chmod +x ./entrypoint.sh

# Opening port 8000:
EXPOSE 8000
CMD ["bash", "./entrypoint.sh"]