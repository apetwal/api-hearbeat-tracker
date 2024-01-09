import time
import sys
import multiprocess
import yaml
from utils import get_http_endpoints, send_request_and_print_status


def background_task(http_endpoint_val, request_timeout,heartbeat_interval):
    while not background_task.cancelled:
        send_request_and_print_status(http_endpoint_val, request_timeout)
        time.sleep(heartbeat_interval)


background_task.cancelled = False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <endpoint_file_path>")
        sys.exit(1)
    endpoint_file_path = sys.argv[1]
    http_endpoints = get_http_endpoints(endpoint_file_path)
    with open('config.yaml') as config_file:
        config_data = yaml.safe_load(config_file)
        print("Configuration parameters")
        print(config_data)
        print()

    process_array = []
    for http_endpoint in http_endpoints:
        process = multiprocess.Process(target=background_task, args=(http_endpoint, config_data["request_timeout"],config_data["heartbeat_interval"]))
        process_array.append(process)
        process.start()
    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        background_task.cancelled = True
        for process in process_array:
            process.terminate()
        print("process successfully closed")
