import requests
from bs4 import BeautifulSoup

# 코로나 요약 현황을 가져오는 함수
def get_corona_summary():
    url = "http://ncov.mohw.go.kr/"
    res = requests.get(url)

    soup = BeautifulSoup(res.text,'lxml')
    patients = soup.select("ul.liveNum span.num")
    #titles = soup.select("ul.liveNum strong.tit")

    #for n in range(0, len(patients)):
    #    print(titles[n].text + ":" + patients[n].text)

    results = {
    '확진환자' : int(patients[0].text.replace(',', '').replace('(누적)', '')),
    '완치' : int(patients[1].text.replace(',', '')),
    '치료중' : int(patients[2].text.replace(',', '')),
    '사망' : int(patients[3].text.replace(',', ''))
    }
    return results

# 테스트 용 코드
if __name__ == "__main__":
    print(get_corona_summary())