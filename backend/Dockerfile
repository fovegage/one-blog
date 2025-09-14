FROM python:3.6

RUN mkdir -p /web

WORKDIR /web

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD . /web

EXPOSE 8866

CMD ["gunicorn", "blogapi.wsgi:application", "-c", "./gunicorn.conf"]
