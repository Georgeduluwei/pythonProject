import requests
import json
from requests_toolbelt import MultipartEncoder
def creatConnent():
    data = MultipartEncoder(fields={'floor_id': '84617'})
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': data.content_type,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/aparthouse/roomhouseadd'
    res = requests.post(url=url, data=data, headers=header)
    roomid = json.loads(res.text)['data']['id']
    print(roomid)

    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/roomcontract/createcontract'
    data = 'room_id='+str(roomid)+'&contract_sort=paper&contract_type=normal&customer_type=personal&customer_company_id=&customer_name=%E5%BC%A0%E4%B8%89&customer_phone=13564549900&emergency_contact_name=&emergency_contact_phone=&customer_id_type=id&customer_id_number=&customer_id_pictures=&nationality=&pictures=&offline_no=&comments=&roommates=%5B%5D&start_time=2022-08-01&end_time=2022-08-31&month_rental=1000&property_amount=&deposit=1000&deposit_code=1&deposit_rule=0&pay_method_f=1&natural_month_order=0&rent_pay_way=advanced&rent_pay_days=0&discount_sort=cycle&discount_type=amount&discount_order=&discount_value=&extra_discount_sort=cycle&extra_discount_type=order&extra_discount_order=&extra_discount_value=&fees=%5B%5D&meterfees=%5B%5D&has_rentfree=0&rentfrees=%5B%5D&ignore_order=&segments=%5B%5D&sign_status=0&source=2&signer_id=&signer_name=&signed_at=2022-09-20&credit_card=&bank=&bank_area=&acceptance_no=&renter_address=&renter_postcodes=&renter_email=&habitancy_type=1'
    res = requests.post(url=url, data=data, headers=header)
    print(res.text)
    contractid = json.loads(res.text)['data']['id']

    '''获取账单token'''
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v2/requesttoken/get'
    res = requests.get(url=url,headers=header)
    print(res.text)
    requestToken = json.loads(res.text)['data']['requestToken']
    print(requestToken)

    '''生成杂费账单'''
    data = MultipartEncoder(fields={'contract_id': str(contractid),'ought_pay_time': '2022-09-20',
                                    'start_time': '2022-09-20','end_time': '2022-09-20','order_fees': '[{"fee_sort":"deposit","fee_type":114,"flow_type":0,"amount":100,"discount_value":0,"roommate_id":"","discount_sort":"cycle","discount_type":"amount","discount_order":null,"pay_method_f":null}]','comments':''})
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': data.content_type,
        'RequestToken': requestToken,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/roomorders'
    res = requests.post(url=url, data=data, headers=header)
    print(res.text)

    '''获取账单ID'''
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/roominfo/getroominfo?room_id='+str(roomid)
    res = requests.get(url=url,headers=header)
    #print(res.text)
    id = json.loads(res.text)['data']['orders']['unpaid'][0]['id']
    print(id)

    '''获取费项ID'''
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/roomorders/'+str(id)
    res = requests.get(url=url,headers=header)
    #print(res.text)
    fee_id1 = str(json.loads(res.text)['data']['order_fees'][0]['id'])
    fee_id2 = str(json.loads(res.text)['data']['order_fees'][1]['id'])
    print(fee_id1,fee_id2)

    '''收款'''
    data = MultipartEncoder(fields={'pay_amount': '2000','pay_method':'alipay','actual_pay_time': '2022-09-20','trade_serial_no':'','receive_payment_comments':'','fees': '[{"id":%s:,"in_amount":100,"is_balance_processing":0},{"id":%s:,"in_amount":100,"is_balance_processing":0}]'%(fee_id1, fee_id2)})
    print(data)
    header = {
        'Authorization':'token 19fdab62a55c3e0084836f187ff2ce0d3851a184',
        'Content-Type': data.content_type,
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
     }
    url = 'https://jz.api.shuidiguanjia.com/api/v4/roomorders/'+str(id)+'/receive_payment'
    print(url)
    res = requests.post(url=url, data=data, headers=header)
    print(111,res.text, res.status_code)

creatConnent()