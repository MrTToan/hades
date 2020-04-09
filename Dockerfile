FROM python:3.7-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

ENV TZ=Asia/Ho_Chi_Minh
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY . .

EXPOSE 8000

ENTRYPOINT ["python3", "manage.py"]
CMD ["runserver"]
