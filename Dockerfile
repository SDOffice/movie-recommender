FROM python:3.6
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
COPY netflix_titles.csv ./
COPY App.py ./
CMD ["python", "/App.py"]
