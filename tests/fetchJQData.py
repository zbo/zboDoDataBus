import jqdatasdk as jq


def login():
    jq.auth('18758561268', '561268')


def get_sh_data(code, start, end, fre):
    data = jq.get_price(security=code, start_date=start, end_date=end, frequency=fre)
    print data


def get_sh_data_detail(code, fre):
    data = jq.get_price(security=code, frequency=fre)
    print data.ix[1].name
    print data.ix[1]['open']


if __name__ == '__main__':
    login()
    get_sh_data('000001.XSHG','2019-04-25', '2019-04-29', '1m')
    get_sh_data_detail('000001.XSHG','1m')
