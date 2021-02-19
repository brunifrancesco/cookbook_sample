# Cookbook sample project

## Getting started

### Install deps

```
pip install -r requirements.txt
```


#### Run celery worker

##### Pull up REDIS

    docker run --rm -ti -p 6379:6379 redis

##### Run worker with the beat

    celery -A cookbook worker -L INFO -B
