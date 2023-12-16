# Standard Library
import multiprocessing

bind = '0.0.0.0:9010'
worker_class = 'uvicorn.workers.UvicornWorker'
preload_app = True
max_requests = 100
max_requests_jitter = 20
workers = multiprocessing.cpu_count() // 2
