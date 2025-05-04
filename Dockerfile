#usinf official Python base image
FROM python:3.10-slim

# setting env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYHTONUNBUFFERED 1

# setting working directory inside container
WORKDIR /app

# copying dependency files
COPY requirements.txt /app/

# installing dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# copying entire Django Project
COPY . /app/

#Running the Django dev server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

