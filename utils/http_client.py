import httpx
from env import env
from utils.error_handler import handle_error
from typing import Optional


class HttpClient:
    def __init__(self):
        self.base_url = env.TALENTLMS_BASE_URL
        self.auth = (env.TALENTLMS_API_KEY, "")  # Basic Auth: (username, password)

    async def get(self, endpoint: str, params: Optional[dict] = None):
        """
        Thực hiện yêu cầu GET bất đồng bộ đến API của TalentLMS với Basic Authentication.
        :param endpoint: Endpoint của API (ví dụ: "courses").
        :param params: Tham số truy vấn (query parameters) dưới dạng dictionary.
        """
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(url, params=params, auth=self.auth)
                response.raise_for_status()  # Nếu mã trạng thái không phải 2xx, raise exception
                return response.json()  # Trả về dữ liệu JSON đã giải mã
            except httpx.HTTPStatusError as http_err:
                handle_error(http_err, response) # type: ignore
            except Exception as err:
                handle_error(err)

    async def post(self, endpoint: str, data: dict):
        """
        Thực hiện yêu cầu POST bất đồng bộ để gửi dữ liệu đến TalentLMS với Basic Authentication.
        """
        url = f"{self.base_url}/{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, json=data, auth=self.auth)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as http_err:
                handle_error(http_err, response) # type: ignore
            except Exception as err:
                handle_error(err)

    async def put(self, endpoint: str, data: dict):
        """
        Thực hiện yêu cầu PUT bất đồng bộ để cập nhật dữ liệu trên TalentLMS với Basic Authentication.
        """
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.put(url, json=data, auth=self.auth)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as http_err:
                handle_error(http_err, response) # type: ignore
            except Exception as err:
                handle_error(err)

    async def delete(self, endpoint: str):
        """
        Thực hiện yêu cầu DELETE bất đồng bộ để xóa dữ liệu trên TalentLMS với Basic Authentication.
        """
        url = f"{self.base_url}{endpoint}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(url, auth=self.auth)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as http_err:
                handle_error(http_err, response) # type: ignore
            except Exception as err:
                handle_error(err)
