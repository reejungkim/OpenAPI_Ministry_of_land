# OpenAPI 
[![Gmail Badge](https://img.shields.io/badge/Gmail-d14836?style=flat-square&logo=Gmail&logoColor=white&link=mailto:reejugn.kim@gmail.com)](mailto:reejung.kim@gmail.com) 
[![Linkedin Badge](https://img.shields.io/badge/-LinkedIn-blue?style=flat-square&logo=Linkedin&logoColor=white&link=www.linkedin.com/in/reejungkim/)](https://www.linkedin.com/in/reejungkim/) 
[![Git page](http://img.shields.io/badge/-Portfolio-black?style=flat-square&logo=github&link=https://reejungkim.github.io/)](https://reejungkim.github.io/)
<br></br>


<!---
```
conda install -c conda-forge xmltodict
```
--->
[공공데이터](https://www.data.go.kr/index.do)

### Reference
<!--- 
- [국토부 한국부동산원_전국 청약 분양정보 상세조회 서비스](https://www.data.go.kr/data/15098547/openapi.do)
```
# Python3 샘플 코드 #

import requests

url = 'http://openapi.reb.or.kr/OpenAPI_ToolInstallPackage/service/rest/ApplyhomeInfoSvc/getLttotPblancList'
params ={'serviceKey' : '서비스키', 'startmonth' : '202101', 'endmonth' : '202103', 'houseSecd' : '01', 'sido' : '강원', 'houseName' : '횡성 벨라시티', 'rentSecd' : '0' }

response = requests.get(url, params=params)
print(response.content)
```

- [국토부 한국수자원공사_토지 분양 정보](https://www.data.go.kr/data/15099019/openapi.do)
- [국토교통부_대지권등록정보조회서비스](https://www.data.go.kr/data/15056691/openapi.do)
- [국토교통부_토지특성정보서비스](https://www.data.go.kr/data/15057558/openapi.do)
--->
- [국토교통부 공동주택가격정보서비스](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057988)

   [View jupyter notebook](https://github.com/reejungkim/OpenAPI_Ministry_of_land/blob/main/%EA%B5%AD%ED%86%A0%EA%B5%90%ED%86%B5%EB%B6%80_%EA%B3%B5%EB%8F%99%EC%A3%BC%ED%83%9D%EA%B0%80%EA%B2%A9%EC%A0%95%EB%B3%B4%EC%84%9C%EB%B9%84%EC%8A%A4.ipynb)
```
import requests

url = 'http://apis.data.go.kr/1611000/nsdi/ApartHousingPriceService/wms/getApartHousingPriceWMS'
params ={'serviceKey' : '서비스키', 'layers' : '163', 'crs' : 'EPSG:5174', 'bbox' : '191000.225,447240.534,191179.03,447423.308', 'width' : '915', 'height' : '700', 'format' : 'image/png', 'transparent' : 'false', 'bgcolor' : '0xFFFFFF', 'exceptions' : 'blank' }

response = requests.get(url, params=params)
print(response.content)
```


| 항목명(국문)  | 항목명(영문)        | 항목크기 | 항목구분 | 샘플데이터               | 항목설명     |
|----------|----------------|------|------|---------------------|----------|
| 고유번호     | pnu            | 19   | 필수   | 1111010100100040007 | 고유번호     |
| 법정동코드    | ldCode         | 10   | 옵션   | 1111010100          | 법정동코드    |
| 법정동명     | ldCodeNm       | 300  | 옵션   | 서울특별시 종로구 청운동       | 법정동명     |
| 특수지구분코드  | regstrSeCode   | 1    | 옵션   | 1                   | 특수지구분코드  |
| 특수지구분명   | regstrSeCodeNm | 300  | 옵션   | 일반                  | 특수지구분명   |
| 지번       | mnnmSlno       | 9    | 옵션   | 1-1                 | 지번       |
| 기준년도     | stdrYear       | 4    | 필수   | 2012                | 기준년도     |
| 기준월      | stdrMt         | 2    | 필수   | 09                  | 기준월      |
| 공동주택코드   | aphusCode      | 10   | 옵션   | 1                   | 공동주택코드   |
| 공동주택구분코드 | aphusSeCode    | 1    | 옵션   | 5                   | 공동주택구분코드 |
| 공동주택구분명  | aphusSeCodeNm  | 300  | 옵션   | 다세대                 | 공동주택구분명  |
| 특수지명     | spclLandNm     | 150  | 옵션   | 상암택지개발사업지구 3-7블럭    | 특수지명     |
| 공동주택명    | aphusNm        | 300  | 옵션   | 상암월드컵7단지            | 공동주택명    |
| 전용면적(㎡)  | prvuseAr       | 20   | 옵션   | 84.45               | 전용면적(㎡)  |
| 공시가격(원)  | pblntfPc       | 13   | 옵션   | 480000000           | 공시가격(원)  |
| 데이터기준일자  | lastUpdtDt     | 10   | 옵션   | 2016-09-26          | 데이터기준일자  |


