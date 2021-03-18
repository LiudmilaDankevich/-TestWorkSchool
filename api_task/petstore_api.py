import requests


class PetstorePet:

    def get_headers(self):
        headers = {
            'Accept: application/ison'
        }
        return headers

    def __init__(self):
        self.base_url = \
            'https://petstore.swagger.io/v2/pet'
        self.headers = self.get_headers()

    def create_pet(self):
        url = self.base_url + '/pet'
        json = {
            "id": 8,
            "category": {
                "id": 8,
                "name": "Roy"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 8,
                    "name": "Roy"
                }
            ],
            "status": "available"
        }
        response = requests.request("POST", url, json=json)
        json_response = response, json()
        assert json_response['code'] == 200, f'{json_response["code"]} not equal code 200'
        print('created')
        return json_response

    def get_pet(self):
        url = self.base_url + '/8'
        json = {
            "id": 8,
            "category": {
                "id": 8,
                "name": "Roy"
            },
            "name": "Roy",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 8,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.request("GET", url, json=json)
        json_response = response, json()
        assert json_response['code'] == 200, f'{json_response["code"]} not equal code 200'
        print('get')
        return json_response

    def delete_pet(self):
        url = self.base_url + '/8'
        json = {
            "id": 8,
            "category": {
                "id": 8,
                "name": "Roy"
            },
            "name": "Roy",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 8,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.request('DELETE', url, json=json)
        json_response = response, json()
        assert json_response['code'] == 200, f'{json_response["code"]} not equal code 200'
        print('deleted')
        return json_response

    def get_pet_2(self):
        url = self.base_url + '/8'
        json = {
            "id": 8,
            "category": {
                "id": 8,
                "name": "Roy"
            },
            "name": "Roy",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 8,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        response = requests.request("GET", url, json=json)
        json_response = response, json()
        assert json_response['code'] == 404, f'{json_response["code"]} not equal code 404'
        print('No')
        return json_response

