# OpenAPI 




```
conda install -c conda-forge xmltodict
```

[공공데이터](https://www.data.go.kr/index.do)

### Reference
- [국토부 한국부동산원_전국 청약 분양정보 상세조회 서비스](https://www.data.go.kr/data/15098547/openapi.do)
- [국토부 한국수자원공사_토지 분양 정보](https://www.data.go.kr/data/15099019/openapi.do)
- [국토교통부_대지권등록정보조회서비스](https://www.data.go.kr/data/15056691/openapi.do)
- [국토교통부_토지특성정보서비스](https://www.data.go.kr/data/15057558/openapi.do)


```
# Python3 샘플 코드 #

import requests

url = 'http://openapi.reb.or.kr/OpenAPI_ToolInstallPackage/service/rest/ApplyhomeInfoSvc/getLttotPblancList'
params ={'serviceKey' : '서비스키', 'startmonth' : '202101', 'endmonth' : '202103', 'houseSecd' : '01', 'sido' : '강원', 'houseName' : '횡성 벨라시티', 'rentSecd' : '0' }

response = requests.get(url, params=params)
print(response.content)
```
