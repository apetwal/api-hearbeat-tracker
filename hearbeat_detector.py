import time
from concurrent.futures import ThreadPoolExecutor
import sys

import yaml

from utils import get_http_endpoints, send_request_and_print_status

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
    with ThreadPoolExecutor(max_workers=config_data["thread_pool_size"]) as executor:
        while True:
            futures = [executor.submit(send_request_and_print_status, http_endpoint,config_data["request_timeout"]) for http_endpoint in
                       http_endpoints]
            for future in futures:
                future.result()
            time.sleep(config_data["heartbeat_interval"])
            print()
