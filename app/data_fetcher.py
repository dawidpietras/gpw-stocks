import pandas as pd
from abc import ABC, abstractmethod
from datetime import datetime

ticker_dict = {
    'XTB': 'xtb',
    'AMICA': 'amc'
}


class GetDataFromUrl(ABC):
    def __init__(self, ticker):
        self.ticker = ticker

    @abstractmethod
    def return_data_list(self):
        pass


class GetDataFromStooq(GetDataFromUrl):
    def __init__(self, ticker):
        super().__init__(ticker)
        self._url = f'https://stooq.com/q/d/l/?s={self.ticker}&i=d'

    def return_data_list(self):
        return list(pd.read_csv(self._url).itertuples(index=False, name=None))


class GetDataFromStooqInTimeRange(GetDataFromStooq):
    def __init__(self, ticker, start_date, end_date=None):
        super().__init__(ticker)
        self.start_date = start_date
        self.end_date = end_date
        self._url = f'https://stooq.com/q/d/l/?s={self.ticker}&d1={self.__start_date}&d2={self.__end_date}&i=d'

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, start_date):
        format_yyyymmdd = '%Y%m%d'
        try:
            datetime.strptime(start_date, format_yyyymmdd)
            self.__start_date = start_date
        except ValueError:
            print("The string is not a date with format " + format_yyyymmdd)
            raise SystemExit

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, end_date):
        format_yyyymmdd = '%Y%m%d'
        if not end_date:
            self.__end_date = datetime.today().strftime(format_yyyymmdd)
        else:
            try:
                datetime.strptime(end_date, format_yyyymmdd)
                self.__end_date = end_date
            except ValueError:
                print("The string is not a date with format " + format_yyyymmdd)
                raise SystemExit

print(GetDataFromStooqInTimeRange('amc', '200303', '20220901').return_data_list())
# mycursor = db.cursor()
# data_list = []
# #
# for row in range(len(df)):
#     # print(df.iloc[row])
#     data_row = tuple((df.iloc[row, 0], round(df.iloc[row, 1], 2), round(df.iloc[row, 2], 2),
#           round(df.iloc[row, 3], 2), round(df.iloc[row, 4], 2),
#           int(df.iloc[row, 5])))
#     print(data_row)
#     data_list.append(data_row)
#
# start_time = time.time()
# mycursor.executemany('''insert into amica (Date, Open, High, Low, Close, Volume)
#                         values (%s,%s,%s,%s,%s,%s)''', data_list)
#
# print(f'Insert {len(df.index)} wierszy trwał: {int(time.time() - start_time)} s.')
# #
# db.commit()
# mycursor.execute('''create table amica (
#  ID int not null primary key auto_increment,
#  Date date,
#  Open decimal(10,2),
#  High decimal(10,2),
#  Low decimal(10,2),
#  Close decimal(10,2),
#  Volume int
#  );''')

#

#
# mycursor.execute('select * from xtb')
# #
# for row in mycursor:
#     print(row)
#     for data in row:
#         if type(data) is Decimal:
#             print(float(data))