import requests


class HttpEndpoint:
    # Dictionary to map request types (GET, PUT, POST, PATCH, DELETE) to corresponding request functions from the
    # 'requests' module
    request_func = {'GET': requests.get, 'PUT': requests.put, 'POST': requests.post, 'PATCH': requests.patch,
                    'DELETE': requests.delete}

    def __init__(self, name, url, method='GET', headers=None, body=None):
        """
               Initializes an HttpEndpoint instance.

               :param name: Name of the HTTP endpoint.
               :param url: URL of the HTTP endpoint.
               :param method: HTTP request method (default is 'GET').
               :param headers: HTTP request headers.
               :param body: HTTP request body.
        """
        self.name = name
        self.url = url
        self.method = method
        self.headers = headers if headers is not None else {}
        self.body = body
        self.total_api_calls_count = 0
        self.successful_api_calls_count = 0

    def send_request(self, request_timeout):
        """
                Sends an HTTP request to the specified endpoint and updates the call counts.

                :param request_timeout: Timeout for the HTTP request.
        """
        self.total_api_calls_count += 1
        try:
            r = self.request_func[self.method](self.url, headers=self.headers, data=self.body, timeout=request_timeout)
            latency = r.elapsed.total_seconds()
            if 200 <= r.status_code <= 300 and latency < 0.5:
                self.successful_api_calls_count += 1
        except requests.ConnectTimeout:
            print(f"{self.url} request_timeout")
