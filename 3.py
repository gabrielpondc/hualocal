import requests

cookies = {
    'b32fe732acea4aa9a34287817ba7b4c4': 'WyIyOTkxMjcxNjk2Il0',
    'c2f61647bf394f4f8f6a2dd4faf2ff74': 'WyIzNzg1MzkzODY2Il0',
    'd377d72df97c4183a234968b9ca517a1': 'WyIxNzAwOTA4MTY0Il0',
    'HW_id_hicloudportal_2_cloud_huawei_com': 'ba8b2574f43d4c5fabb37368f683a322',
    'HW_idts_hicloudportal_2_cloud_huawei_com': '1608638988510',
    'HW_idn_hicloudportal_2_cloud_huawei_com': 'fb988bd831f142c1a9c2bdcf77f6b428',
    'HuaweiID_CAS_ISCASLOGIN': 'true',
    'CASLOGINSITE': '1',
    'LOGINACCSITE': '1',
    'HW_viewts_hicloudportal_2_cloud_huawei_com': '1608639021436',
    'siteID': '1',
    'loginID': 'F2F3E4CBAB0E55C8B9AE4336B1CD7F30',
    'token': 'f6ef748bd56257e7a9aecfb05f8b1cec5286c4389b7675e9',
    'cplang': 'zh-cn',
    'isLogin': '1',
    'loginSecLevel': '0',
    'functionSupport': '1_1',
    'userId': '2850086000373027919',
    'webOfficeEditToken': '28500860003730279191608639023131',
    'logId': '666ef4a10da452b8-35bffbad05209e19',
    'HW_refts_hicloudportal_2_cloud_huawei_com': '1608639023675',
    'HW_idvc_hicloudportal_2_cloud_huawei_com': '2',
    'CSRFToken': 'c0ef126304e16fb8b2bd25aa7f5e9f2a4f65e16e1cae5422',
    'JSESSIONID': '692F47A2CAB3620D1B7A506F20968EAE',
}

headers = {
    'Connection': 'keep-alive',
    'x-hw-account-brand-id': '0',
    'CSRFToken': 'c0ef126304e16fb8b2bd25aa7f5e9f2a4f65e16e1cae5422',
    'x-hw-device-manufacturer': 'HUAWEI',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66',
    'Accept': 'application/json, text/plain, */*',
    'x-hw-device-brand': 'HUAWEI',
    'userId': '2850086000373027919',
    'x-hw-app-brand-id': '1',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://cloud.huawei.com/home',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
}

params = (
    ('checkType', '1'),
    ('traceId', '07100_02_1608639083_25738929'),
)

response = requests.get('https://cloud.huawei.com/heartbeatCheck', headers=headers, params=params, cookies=cookies)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://cloud.huawei.com/heartbeatCheck?checkType=1&traceId=07100_02_1608639083_25738929', headers=headers, cookies=cookies)
