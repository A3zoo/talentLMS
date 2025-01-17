import logging
import requests  # Import từ thư viện requests, không phải fastapi.requests

def handle_error(error, response=None):
    """
    Xử lý lỗi khi gọi API, có thể là lỗi HTTP hoặc lỗi khác.
    """
    if isinstance(error, requests.exceptions.HTTPError):  # Đúng cách gọi exceptions
        # Lỗi HTTP
        status_code = response.status_code if response else None
        print(f"HTTP Error: {status_code} - {error}")
        logging.error(f"HTTP Error: {status_code} - {error}")
        if response is not None:
            print(f"Response body: {response.text}")
            logging.error(f"Response body: {response.text}")
    else:
        # Lỗi chung khác
        print(f"Error occurred: {error}")
        logging.error(f"Error occurred: {error}")
