FROM python:3.11-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# نصب پکیج‌های لازم برای به‌روزرسانی SQLite
RUN apt-get update && apt-get install -y wget build-essential libreadline-dev

# دانلود و نصب SQLite 3.31 یا جدیدتر
RUN wget https://www.sqlite.org/2020/sqlite-autoconf-3310100.tar.gz && \
    tar xvfz sqlite-autoconf-3310100.tar.gz && \
    cd sqlite-autoconf-3310100 && \
    ./configure && \
    make && \
    make install

# تنظیم مجدد لینک‌های دینامیک و پاکسازی
RUN ldconfig
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . /app/

CMD ["python3", "core/manage.py", "runserver", "0.0.0.0:8000"]
