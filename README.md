# API Hearbeat Tracker
This Python script is designed to monitor the availability of HTTP endpoints by sending periodic requests and calculating 
the availability percentage based on the responses. It utilizes concurrent execution with a thread pool for efficiency.

### Files
**http_endpoint.py->** Defines the HttpEndpoint class, representing an HTTP endpoint with methods to send requests and track
availability statistics.

**utils.py->** Contains utility functions for reading HTTP endpoint configurations from a YAML file and sending requests to 
endpoints.

**heartbeat_detector.py->** The main script that reads endpoint configurations, initiates monitoring, and prints availability 
percentages over time.

**config.yaml->** Configuration file specifying parameters such as the thread pool size and request timeout.

**requirements.txt->** Lists required Python packages and their versions. Install these dependencies using pip install -r requirements.txt.

### Usage

1. Install dependencies using the following command:
    ```bash
    pip install -r requirements.txt
    ```

2. Run the script with the following command:
    ```bash
    python heartbeat_detector.py <endpoint_file_path>
    ```
   Replace `<endpoint_file_path>` with the path to your YAML file containing HTTP endpoint configurations.


3. The script will continuously monitor the specified endpoints, printing their availability percentages every 5 seconds.

### Configuration

Modify the `config.yaml` file to adjust parameters like thread pool size and request timeout according to your requirements.

### Endpoint Configuration

Create a YAML file similar to `sampleendpoint_test.yaml` to define the HTTP endpoints you want to monitor. 
Include details such as name, URL, HTTP method, headers, and request body if applicable. To test a sample yaml file is 
present in the folder api_endpoints_conf
