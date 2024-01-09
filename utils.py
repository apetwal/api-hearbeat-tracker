import yaml
from http_endpoint import HttpEndpoint


def get_http_endpoints(file_path):
    """
        Reads a YAML file containing HTTP endpoint data and returns an array of HttpEndpoint instances.

        :param file_path: Path to the YAML file containing endpoint data.
        :return: Array of HttpEndpoint instances.
    """
    with open(file_path) as f:
        data_map = yaml.safe_load(f)
        http_endpoint_array = []
        for endpoint_data in data_map:
            endpoint = HttpEndpoint(
                name=endpoint_data['name'],
                url=endpoint_data['url'],
                method=endpoint_data.get('method', 'GET'),
                headers=endpoint_data.get('headers', {}),
                body=endpoint_data.get('body', None)
            )
            http_endpoint_array.append(endpoint)
        return http_endpoint_array


def send_request_and_print_status(http_endpoint,request_timeout):
    """
        Sends an HTTP request to an endpoint and prints its availability status.

        :param http_endpoint: HttpEndpoint instance.
        :param request_timeout: Timeout for the HTTP request.
    """
    http_endpoint.send_request(request_timeout)
    availability_percentage = 100.0 * (http_endpoint.successful_api_calls_count / http_endpoint.total_api_calls_count)
    print(f'{http_endpoint.url} has {availability_percentage}% availability percentage ')