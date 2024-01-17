FROM python:3.10.9

# Copy analysis scripts
COPY . /app
WORKDIR /app

# install package
RUN pip install -r requirements.txt 

# run the main
CMD ["python", "main.py"]

