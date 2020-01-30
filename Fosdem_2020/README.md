## Redis installation

Installed by your distribution package manager or manually :

```
$ wget http://download.redis.io/releases/redis-5.0.7.tar.gz
$ tar xvzf redis-5.0.7.tar.gz
$ cd redis-5.0.7
$ make
$ ./src/redis-server
```

## Python requirements

Requires `Py3.6` at least :

```
$ git clone https://github.com/ncrocfer/talks
$ cd talks/Fosdem_2020/
$ virtualenv -p python3.6 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Speaker

- Celery demonstration

```
$ jupyter notebook celery.ipynb > /tmp/notebook.log 2>&1 &
$ celery worker -A tasks --loglevel=INFO
```

- Director demo

Just follow the `director` notebook.
