import configuration
import requests
import data


def post_order_create():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.order_json,
                         headers=data.headers_client)

def get_order_by_track(track):
    return requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK, params={"t": track})