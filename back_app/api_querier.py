import urllib.parse
from typing import Optional, Dict, Callable, Union

import requests


def get_response_content(download_url: str) -> Optional[bytes]:
    def get_content(response: requests.Response) -> Optional[bytes]:
        if 200 <= response.status_code <= 250:
            return response.content
        else:
            return None
    return get_response(download_url, get_content)


def get_response_json(download_url: str) -> Optional[Dict]:
    def get_json(response: requests.Response) -> Optional[Dict]:
        if 200 <= response.status_code <= 250:
            return response.json()
        else:
            return None
    return get_response(download_url, get_json)


def get_response(download_url: str, response_get_prop: Callable) -> Union[Optional[bytes], Optional[Dict]]:
    response = requests.get(download_url)
    return response_get_prop(response)


def send_post(url: str, content: Dict) -> requests.Response:
    return requests.post(url, content)


def send_post_get_response_text(url: str, content: Dict) -> str:
    response = send_post(url, content)
    if 200 <= response.status_code <= 250:
        return response.text
    else:
        return "Error {}".format(response.status_code)


def map_parameters(**params) -> str:
    parameters = ""
    if params:
        clean_params = remove_empty_values_from_dict(params)
        parameters = "&".join([f"{urllib.parse.quote(k)}={urllib.parse.quote(v)}" for (k, v) in clean_params.items()])
    return parameters


def remove_empty_values_from_dict(d: Dict) -> Dict:
    return {key: value for (key, value) in d.items() if value}
