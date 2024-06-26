from redis import Redis
from rq import Queue, Worker
from config import Config
from datetime import datetime
from app import create_app

app = create_app(is_redis=True)
app.app_context().push()

redis = Redis.from_url(Config.REDIS_URL)
queue = Queue(Config.REDIS_QUEUE_NAME, connection=redis)
worker_name = datetime.now().strftime("%Y%m%d_%H%M%S")
worker = Worker([queue], connection=redis, name=worker_name)
worker.work()
