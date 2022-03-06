# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.0

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Get the Real World example app
#RUN git clone https://github.com/tagutaj/ptfuserapi.git
RUN git config --global git.protocol https
RUN git config --global user.email tagutaj@gmail.com
RUN git config --global user.name tagutaj
RUN export GITHUB_TOKEN=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



RUN git clone git@github.com:tagutaj/ptfuserapi

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /userapi

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /userapi

EXPOSE 8080

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]