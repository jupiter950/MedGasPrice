import requests
import json
from socketapp.models import GasData, MedGasPrice
from socketapp.serializers import GasSerializer, MedGasPriceSerializer

def crape_data():
    headers = {"Content-Type": "application/json; charset=utf-8",
                   "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTEwODIwNDUsImV4cCI6MTcxMTI1NDg0NSwiaXNzIjoiUm91dGVzY2FuQXBpIiwic3ViIjoiNDUuMTI2LjMuMjUyIn0._GR9VFjPpS9nGfv--B7Y_n3sG-nBP38YDdswAvKjYAY"}
    cookies = {
        'routescan_api_jwt': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MTExMDU3NjUsImV4cCI6MTcxMTI3ODU2NSwiaXNzIjoiUm91dGVzY2FuQXBpIiwic3ViIjoiNDUuMTI2LjMuMjUyIn0.PQGdIQUsmqJrObDaj6T5hFS7pFlBFq6CqrHeZF5t6UI',
        'route_api_jwt_enabled': 'true'
    }
    res = requests.get('https://cdn.routescan.io/api/evm/all/aggregations/avg-gas-price?ecosystem=avalanche', headers=headers)
    med_res = requests.get('https://snowtrace.io/_next/data/routescan:mainnet:0f1d55814801ee30133ef6640adfa630909f8215/gastracker.json', cookies=cookies)
    # print(json.loads(med_res.text)["pageProps"])
    # print(json.loads(med_res.text)["pageProps"]["values"]["low"])

    print(json.loads(res.text)[0])
    GasData.objects.all().delete()
    for item in json.loads(res.text):
        serializer = GasSerializer(data={
            'price_date' : item[1],
            'price' : item[0]
        })
        if serializer.is_valid(raise_exception=True):
            serializer.save()
    MedGasPrice.objects.all().delete()
    serializer_med = MedGasPriceSerializer(data={
        'low': json.loads(med_res.text)["pageProps"]["values"]["low"],
        'high': json.loads(med_res.text)["pageProps"]["values"]["high"],
        'avg': json.loads(med_res.text)["pageProps"]["values"]["avg"]
    })
    if serializer_med.is_valid(raise_exception=True):
        serializer_med.save()