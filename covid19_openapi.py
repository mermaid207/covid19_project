import requests
from pprint import pprint
from datetime import date, timedelta
import xmltodict
import json

def get_city_data():
    url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"

    params ={
        'serviceKey':'r7RBwtU4dmlZY2OKG8vW9rZcfhtkcx0lDR62C4EMRdZwgeub8Mb+DfhTExcunb21eH6bem4KY7Uyn9ZSSYC3Wg==',
        'pageNo': '1',
        'numOfRows': '30',
        'startCreateDt' : '20210502',
        'endCreateDt' : '20210503',
    }
    res = requests.get(url, params=params)
    dict_data = xmltodict.parse(res.text)

    json_data = json.dumps(dict_data)
    dict_data = json.loads(json_data)

    pprint(dict_data['response']['body']['items']['item'][0]['gubun'])
    return dict_data
