import json
from time import sleep
from json import dumps
from kafka import KafkaProducer
import requests

Topic = 'my-topic1'
server = ['localhost:9092']

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer = lambda x: dumps(x).encode('utf-8'))
currency = {}
while True:
    request_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    api_response = requests.get(request_url)
    print(api_response.status_code)
    data = api_response.text
    parse_json = json.loads(data)

    usd_val = parse_json['bpi']["USD"]["rate"]
    gbp_val = parse_json['bpi']["GBP"]["rate"]
    eur_val = parse_json['bpi']["EUR"]["rate"]
    currency["USD"] = usd_val
    currency["GBP"] = gbp_val
    currency["EUR"] = eur_val

    print(currency)
    producer.send(Topic, value=currency)
    sleep(10)

