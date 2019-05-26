import request_m
from datetime import datetime, timedelta, date


class DefAction:
    def __init__(self, input_info, currency, today):
        self.input_info = input_info
        self.currency = currency
        self.today = today

    def form_request(self):
        if self.input_info == "today":
            self.today = "".join(str(date.today()).split("-"))
            return request_m.Request(self.today, self.currency).get_info()
        elif self.input_info == "week":
            start = self.today - timedelta(days=self.today.weekday())
            return self.form_dct(start)
        elif self.input_info == "month":
            start = "{1}-{0}-01".format(str(self.today)[5:7], str(self.today)[:4])
            start = datetime.strptime(start, '%Y-%m-%d').date()
            return self.form_dct(start)
        elif self.input_info == "quarter":
            curmonth = str(self.today)[5:7]
            winter = ["12", "01", "02"]
            spring = ["03", "04", "05"]
            summer = ["06", "07", "08"]
            fall = ["09", "10", "11"]
            year = str(self.today)[:4]
            if curmonth in winter:
                month = winter[0]
                year = str(int(str(self.today)[:4]) - 1)
            elif curmonth in spring:
                month = spring[0]
            elif curmonth in summer:
                month = summer[0]
            elif curmonth in fall:
                month = fall[0]
            else:
                month = curmonth
            start = "{1}-{0}-01".format(month, year)
            start = datetime.strptime(start, '%Y-%m-%d').date()
            return self.form_dct(start)
        elif self.input_info == "year":
            start = "{}-01-01".format(str(self.today)[:4])
            start = datetime.strptime(start, '%Y-%m-%d').date()
            return self.form_dct(start)
        else:
            raise ValueError

    def form_dct(self, start):
        date = []
        value = []
        fdate = start
        ndate = start.strftime("%Y%m%d")
        currency = request_m.Request(ndate, self.currency).get_info()[1]
        while fdate != self.today:
            date.append(fdate)
            value.append(request_m.Request(ndate, self.currency).get_info()[0])
            fdate = fdate + timedelta(days=1)
            ndate = fdate.strftime("%Y%m%d")
        else:
            date.append(self.today)
            value.append(request_m.Request(self.today.strftime("%Y%m%d"), self.currency).get_info()[0])
        return date, value, currency
