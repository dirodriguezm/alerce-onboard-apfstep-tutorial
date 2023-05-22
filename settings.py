##################################################
#       tutorial   Settings File
##################################################
import os

## Set the global logging level to debug
LOGGING_DEBUG = True

CONSUMER_CONFIG = {
    "CLASS": "apf.consumers.JSONConsumer",
    "FILE_PATH": os.getenv("CONSUMER_FILE_PATH", "../data/consumer_input.json"),
}
PRODUCER_CONFIG = {
    "CLASS": "apf.producers.JSONProducer",
    "FILE_PATH": os.getenv("PRODUCER_FILE_PATH", "../data"),
    "buffer_size": 5,
}
METRICS_CONFIG = {
    "CLASS": "apf.metrics.LogfileMetricsProducer",
    "PARAMS": {
        "PATH": os.getenv("METRICS_FILE_PATH", "../data/metrics.txt"),
    },
}
PROMETHEUS = False

## Step Configuration
STEP_CONFIG = {
    "CONSUMER_CONFIG": CONSUMER_CONFIG,
    "PRODUCER_CONFIG": PRODUCER_CONFIG,
    "METRICS_CONFIG": METRICS_CONFIG,
    "PROMETHEUS": PROMETHEUS,
}
