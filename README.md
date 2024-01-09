# API Hearbeat Tracker
This Python script is designed to monitor the availability of HTTP endpoints by sending periodic requests and calculating 
the availability percentage based on the responses. Here I have provided two different multi threading approach to solve this 
problem.
1. **Using ThreadPool** - In this approach, a ThreadPoolExecutor is used to create a pool of worker threads that concurrently 
send HTTP requests to different endpoints. The send_request_and_print_status function is submitted to the executor 
for each HTTP endpoint, and the main thread periodically sleeps based on the heartbeat interval.


2. **Using Multiprocess framework** - This approach uses multiprocessing to create separate processes for each HTTP 
endpoint. A background task is defined, and a separate process is spawned for each endpoint, executing this task. 
The main process then sleeps based on the heartbeat interval.

### Which approach to use
**ThreadPoolExecutor:**  It minimizes resource overhead by sharing memory space within a single process, making it a 
lightweight option suitable for scenarios with limited resources. However, it is constrained by the Global Interpreter 
Lock (GIL), impacting performance for CPU-bound tasks, Managing threads is generally simpler than managing separate 
processes.

**Multiprocess framework:** Multiprocessing is advantageous for CPU-bound tasks, as it allows processes to run 
independently in separate memory spaces, effectively utilizing multiple CPU cores. This approach offers better isolation
and fault tolerance, crucial for applications with stringent requirements. While it incurs higher memory overhead due to
separate processes, it excels in scenarios where parallelization and performance on multi-core systems are essential.

### Files
**http_endpoint.py->** Defines the HttpEndpoint class, representing an HTTP endpoint with methods to send requests and track
availability statistics.

**utils.py->** Contains utility functions for reading HTTP endpoint configurations from a YAML file and sending requests to 
endpoints.

**heartbeat_detector.py->** The main script that reads endpoint configurations, initiates monitoring, and prints availability 
percentages over time using threadpool.

**heartbeat_detector_v2.py->** The main script that reads endpoint configurations, initiates monitoring, and prints availability 
percentages over time using multiprocess framework.

**config.yaml->** Configuration file specifying parameters such as the thread pool size and request timeout.

**requirements.txt->** Lists required Python packages and their versions. Install these dependencies using pip install -r requirements.txt.

### Usage

1. Install dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the script with the following command (choose one of the script):
    ```bash
<<<<<<< HEAD
    python heartbeat_detector/heartbeat_detector_v2.py <endpoint_file_path>
=======
    python heartbeat_detector.py <endpoint_file_path>
>>>>>>> 3a3c888a8a1fe0e72ae5621a4f9690ca5a124741
    ```
   Replace `<endpoint_file_path>` with the path to your YAML file containing HTTP endpoint configurations.


3. The script will continuously monitor the specified endpoints, printing their availability percentages every 5 seconds.

### Configuration

Modify the `config.yaml` file to adjust parameters like thread pool size and request timeout according to your requirements.

### Endpoint Configuration

Create a YAML file similar to `sampleendpoint_test.yaml` to define the HTTP endpoints you want to monitor. 
Include details such as name, URL, HTTP method, headers, and request body if applicable. To test a sample yaml file is 
present in the folder api_endpoints_conf
