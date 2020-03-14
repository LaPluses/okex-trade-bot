import httpx
import json
import hmac
import base64
from config import OK_ACCESS_KEY, OK_ACCESS_PASSPHRASE
from enum import Enum


class _RequestMethod(Enum):
    GET = 1
    POST = 2

    def __str__(self):
        if self is _RequestMethod.GET:
            return 'GET'
        else:
            return 'POST'


class _APIProvider:
    __slots__ = {
        '__http_address',
        '__websocket_address',
        '__async_client',
        '__api_key',
        '__secret_key',
        '__passphrase',
    }

    def __init__(
        self,
        http_address: str,
        websocket_address: str,
        api_key: str,
        secret_key: str,
        passphrase: str,
    ):
        self.__http_address = http_address
        self.__websocket_address = websocket_address
        self.__async_client = httpx.AsyncClient(
            http2=True,
            headers={
                OK_ACCESS_KEY: api_key,
                OK_ACCESS_PASSPHRASE: passphrase,
            }
        )
        self.__api_key = api_key
        self.__secret_key = secret_key
        self.__passphrase = passphrase

    def signature(
        self,
        timestamp: int,
        method: _RequestMethod,
        request_path: str,
        body: dict,
    ):
        if str(body) == '{}' or str(body) == 'None':
            body = ''
        message = str(timestamp) + str(method).upper() + \
            request_path + str(body)
        mac = hmac.new(bytes(self.__secret_key, encoding='utf8'), bytes(
            message, encoding='utf-8'), digestmod='sha256')
        d = mac.digest()
        return base64.b64encode(d)

    async def __del__(self):
        await self.__async_client.aclose()
