import re
import requests
import json
from datetime import datetime
from dateutil.relativedelta import relativedelta
from console.domain.Visitor import Visitor, Visitable
from abc import ABC, abstractmethod


class CodeRule(Visitor, ABC):
    def __init__(self, idx):
        self.idx = idx

    @abstractmethod
    def check(self, visitable):
        pass

    def compare(self, visitable, ocr_code, message=''):
        # Rule check & 결과 추가
        if visitable.rule_list[self.idx]['value1'] == ocr_code:
            visitable.rule_list[self.idx]['result'] = 'SUCCESS'
        else:
            visitable.rule_list[self.idx]['result'] = 'FAILURE'

        visitable.rule_list[self.idx]['message'] = message


class FamilyMember(CodeRule):
    def check(self, visitable):
        print("\ncheck {}".format(__class__))

        self.compare(visitable, '01')


class FamilyRelation(CodeRule):
    def check(self, visitable):
        print("\ncheck {}".format(__class__))

        self.compare(visitable, '01')


class BizRegAuthenticity(CodeRule):
    def __init__(self, idx):
        self.idx = idx
        self.decodingKey = '14jJxjX5L5T6pUQTVHm1O8ikppmla4dUpXlJqFeTq8Z+oZRYzGo/3zn2V2RpMshFHagaFadviau9L2kp71vhIg=='

    def check(self, visitable: Visitable):
        print("\ncheck {}".format(__class__))

        # 공공데이터포탈 사업자등록증 진위확인 연동
        result = self.check_biz_validate(visitable.extract_items[0]['register_num'],
                                         visitable.extract_items[0]['opening_date'],
                                         visitable.extract_items[0]['representative'],
                                         visitable.extract_items[0]['name'],
                                         )
        print("사업자등록증 진위확인 연동결과: {}".format(result))

        # 비교 & 결과 등록
        if result:
            self.compare(visitable, result[0]['valid'], result[0]['valid_msg'])
        else:
            print("공공데이터 포털 API 연동 error!!")

    def check_biz_validate(self, b_no, start_dt, p_nm, b_nm):
        result_data_list = {}
        data = {}

        b_data = {"b_no": re.sub(r'[^0-9]', '', b_no),
                  "start_dt": start_dt,
                  "p_nm": p_nm,
                  "p_nm2": "",
                  "b_nm": b_nm,
                  "corp_no": "",
                  "b_sector": "",
                  "b_type": ""}
        dict_data = {}
        dict_data["businesses"] = [b_data]
        data = json.dumps(dict_data)

        if data:
            url = "https://api.odcloud.kr/api/nts-businessman/v1/validate"

            headers = {'Accept': 'application/json',
                       'Authorization': self.decodingKey,
                       'Content-Type': 'application/json'
                       }

            params = {'serviceKey': self.decodingKey}

            r = requests.post(url=url, headers=headers, params=params, data=data, timeout=3)

            if r.status_code == 200:
                result_data_list = r.json()["data"]
                # print(result_data_list)
                for result in result_data_list:
                    b_no = result['b_no']
                    valid = result['valid']
                    request_param = result['request_param']

                    if valid == '01':
                        status = result['status']
                        b_stt = status['b_stt']
                        b_stt_cd = status['b_stt_cd']
                        end_dt = status['end_dt']
                        tax_type = status['tax_type']

                        # print(status)
                        print('사업자번호 : [{}], 대표자성명 : [{}], 개업일자 : [{}], 상호 : [{}]\n- [True] {} 입니다.'.format(
                            request_param['b_no'], request_param['p_nm'], request_param['start_dt'],
                            request_param['b_nm'], tax_type))
                    else:
                        valid_msg = result['valid_msg']
                        print('사업자번호 : [{}], 대표자성명 : [{}], 개업일자 : [{}], 상호 : [{}]\n- [False] {}'.format(
                            request_param['b_no'], request_param['p_nm'], request_param['start_dt'],
                            request_param['b_nm'], valid_msg))

        return result_data_list


class BizRegStatus(CodeRule):
    def __init__(self, idx):
        self.decodingKey = '14jJxjX5L5T6pUQTVHm1O8ikppmla4dUpXlJqFeTq8Z+oZRYzGo/3zn2V2RpMshFHagaFadviau9L2kp71vhIg=='
        self.idx = idx

    def check(self, visitable: Visitable):
        print("\ncheck {}".format(__class__))

        # 공공데이터포탈 사업자등록증 상태조회 연동
        result = self.check_biz_status(visitable.extract_items[0]['register_num'])
        print("사업자등록증 상태조회 연동결과: {}".format(result))

        # 비교 & 결과 등록
        if result:
            self.compare(visitable, result[0]['b_stt_cd'], result[0]['b_stt'])
        else:
            print("공공데이터 포털 API 연동 error!!")

    def check_biz_status(self, b_no):
        '''
        사업자등록 상태조회
        :param b_no: (str) or (list) 사업자등록번호 (필수)
        :return: (dict)
        '''
        b_no_list = []
        result_data_list = {}

        url = "https://api.odcloud.kr/api/nts-businessman/v1/status"

        headers = {'Accept': 'application/json',
                   'Authorization': self.decodingKey,
                   'Content-Type': 'application/json'
                   }

        params = {'serviceKey': self.decodingKey}

        if type(b_no) == list:
            b_no_list = b_no
        else:
            b_no_list.append(b_no)

        # 문자열에서 숫자만 추출 (847-160-0680 => 8471600680)
        for idx, pick_b_no in enumerate(b_no_list):
            b_no_list[idx] = re.sub(r'[^0-9]', '', pick_b_no)

        dict_data = {}
        dict_data["b_no"] = b_no_list
        data = json.dumps(dict_data)

        r = requests.post(url=url, headers=headers, params=params, data=data, timeout=3)

        if r.status_code == 200:
            result_data_list = r.json()["data"]
            for result in result_data_list:
                b_no = result['b_no']
                b_stt = result['b_stt']
                b_stt_cd = result['b_stt_cd']
                end_dt = result['end_dt']
                tax_type = result['tax_type']

                if b_stt:
                    # 계속사업자
                    if b_stt_cd == '01':
                        print('사업자번호 : [{}] \n- {} 입니다.'.format(b_no, tax_type))
                    elif b_stt_cd == '03':
                        print('사업자번호 : [{}] \n- 폐업자 (과세유형:{}, 폐업일자:{}) 입니다.'.format(b_no, b_stt, end_dt))
                    else:
                        print('사업자번호 : [{}] \n- 과세유형:{}, 폐업일자:{} 입니다.'.format(b_no, b_stt, end_dt))
                else:
                    print('사업자번호 : [{}] >> {}'.format(b_no, tax_type))
        else:
            print(r.status_code)

        return result_data_list


class PeriodRule(Visitor, ABC):
    def __init__(self, idx):
        self.idx = idx

    @abstractmethod
    def check(self, visitable: Visitable):
        pass

    def compare(self, visitable: Visitable, ocr_date):

        std_date = ocr_date
        today = datetime.today()
        value = int(visitable.rule_list[self.idx]['value1'])
        unit = visitable.rule_list[self.idx]['value2']
        range = visitable.rule_list[self.idx]['value3']

        # 일/주/월/년 단위별 날짜 계산
        if unit == '01':
            compare_date = today - relativedelta(days=value)
        elif unit == '02':
            compare_date = today - relativedelta(weeks=value)
        elif unit == '03':
            compare_date = today - relativedelta(months=value)
        elif unit == '04':
            compare_date = today - relativedelta(years=value)

        print("규칙(DB)적용일:  [{}]".format(compare_date.strftime('%Y%m%d')))
        print("OCR 추출 기준일: [{}]".format(std_date))

        # 범위에 따른 비교 연산
        if range == '01':  # 초과
            result = compare_date.strftime('%y%m%d') > std_date
        elif range == '02':  # 미만
            result = compare_date.strftime('%y%m%d') < std_date
        elif range == '03':  # 이상
            result = compare_date.strftime('%y%m%d') >= std_date
        elif range == '04':  # 이하
            result = compare_date.strftime('%y%m%d') <= std_date

        print(result)
        if result:
            visitable.rule_list[self.idx]['result'] = 'SUCCESS'
            visitable.rule_list[self.idx]['message'] = ''
        else:
            visitable.rule_list[self.idx]['result'] = 'FAILURE'
            visitable.rule_list[self.idx]['message'] = '설정된 기간에 맞지 않습니다.'


class FamilyRelIssuedPeriod(PeriodRule):
    def check(self, visitable: Visitable):
        print("\ncheck {}".format(__class__))
        self.compare(visitable, visitable.extract_items['issued_date'])


class BizRegOpeningPeriod(PeriodRule):
    def check(self, visitable: Visitable):
        print("\ncheck {}".format(__class__))
        self.compare(visitable, visitable.extract_items['opening_date'])


class BizRegIssuedPeriod(PeriodRule):
    def check(self, visitable: Visitable):
        print("\ncheck {}".format(__class__))
        self.compare(visitable, visitable.extract_items['issued_date'])
