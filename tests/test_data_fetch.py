import pytest
from datetime import datetime
from app.data_fetcher import GetDataFromStooqInTimeRange, GetDataFromStooq


@pytest.fixture
def stooq():
    return GetDataFromStooq('amc')


@pytest.mark.parametrize("stock_name, start_date, end_date", [
    ('amc', '20220111', '20220813'),
    ('amc', '20220117', '20220817'),
    ('amc', '20220303', '20220901'),
])
def test_stooq_in_time_frames(stock_name, start_date, end_date):
    stooq_transactions = GetDataFromStooqInTimeRange(stock_name, start_date, end_date)
    data = stooq_transactions.return_data_list()
    print(datetime.strftime(datetime.strptime(start_date, '%Y%m%d'), '%Y-%m-%d'))
    print(data[0][0])
    assert data[0][0] == datetime.strftime(datetime.strptime(start_date, '%Y%m%d'), '%Y-%m-%d')

