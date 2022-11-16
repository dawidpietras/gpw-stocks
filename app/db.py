import mysql.connector
import os
from dotenv import load_dotenv
from abc import ABC, abstractmethod
from datetime import datetime


load_dotenv('.env')

HOST = os.environ.get("HOST")
USER = os.environ.get("USER")
PASSWD = os.environ.get("PASSWD")
DATABASE = os.environ.get("DATABASE")


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBManager:
    def __init__(self, host, user, passwd, database):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.db = None

    def __enter__(self):
        try:
            self.db = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd,
                database=self.database
            )
            return self.db.cursor()
        except Exception as e:
            print(e)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            return None


class QueryExecutor(ABC):
    """General abstraction for executing query to database."""
    @abstractmethod
    def execute_query(self, query: str):
        pass


class DataValidator(ABC):
    """General abstraction for validation of date provided to database."""
    @abstractmethod
    def is_data_correct(self, validated_input: str):
        pass


class DateFormatValidator(DataValidator):

    """Class provides validation functionality for given date and format."""
    def __init__(self, formats='%Y-%m-%d'):
        self.format = formats

    def is_data_correct(self, validated_input):

        try:
            if validated_input:
                datetime.strptime(validated_input, self.format)

            return True
        except ValueError:
            print("The string is not a date with format " + self.format)
            return False


class ValidatorException(Exception):
    pass


class DataBaseColumnDataTypeValidator(DataValidator):

    """Class validates if data types in given input is equal to data types in table."""
    def __init__(self, data_type_from_table):
        self.data_type_from_table = data_type_from_table

    def is_data_correct(self, validated_input: str):
        if len(self.data_type_from_table == validated_input):
            for i in range(len(validated_input)):
                if self.data_type_from_table[i] == validated_input[1]:
                    continue
                else:
                    raise ValidatorException("Types of given datatypes are not equal. No possibility to insert data.")
        else:
            raise ValidatorException("Length of given datatypes are not equal. No possibility to insert data.")

        return True


class SQLQueryExecutor(QueryExecutor):

    """Class needs context manager responsible for database connection to perform given query execution"""
    def __init__(self, context_manager: DBManager):
        self.context_manager = context_manager

    def execute_query(self, sql_query):
        with self.context_manager as db:
            db.execute(sql_query)
            result = db.fetchall()
            print(result)
            return result


class GetColumnNameAndTypeFromTable:

    """Class returns all column and its type from given table."""
    def __init__(self, query_executor: QueryExecutor):
        self.query_executor = query_executor

    def get_data(self, table):
        sql = f"SELECT COLUMN_NAME, DATA_TYPE FROM information_schema.columns Where (TABLE_NAME = '{table}');"
        self.query_executor.execute_query(sql)


class SelectDataFromDBByDate:
    """Class returns data from table from specific date as well as from range of dates."""
    def __init__(self, query_executor: QueryExecutor, validator: DataValidator):
        self.query_executor = query_executor
        self.validator = validator

    def select_one_date(self, date, table):
        if self.validator.is_data_correct(date):
            sql = f"select * from {table} where date = '{date}'"
            self.query_executor.execute_query(sql)

    def select_date_range(self, start_date, end_date, table):
        if self.validator.is_data_correct(start_date) and self.validator.is_data_correct(end_date):
            sql = f"select * from {table} where date BETWEEN '{start_date}' AND '{end_date}'"
            self.query_executor.execute_query(sql)

    def select_date_from_beginning_to_specific_date(self):
        """TBD"""
        pass


class InsertDataToDB:
    """Insert data or set of data into table."""

    def __init__(self, query_executor: QueryExecutor, validator: DataValidator):
        self.query_executor = query_executor
        self.validator = validator

    def insert_single_row(self, row: list):
        if self.validator.is_data_correct(row):
            sql = f""
            self.query_executor.execute_query(sql)

    def insert_multiple_rows(self, rows: list):
        if self.validator.is_data_correct(rows):
            sql = f""
            self.query_executor.execute_query(sql)


if __name__ == '__main__':
    context = DBManager(HOST, USER, PASSWD, DATABASE)
    query_manager = SQLQueryExecutor(context)
    validators = DateFormatValidator()
    SelectDataFromDBByDate(query_manager, validators).select_date_range('2020-08-12', '2020-08-14', 'xtb')
    SelectDataFromDBByDate(query_manager, validators).select_one_date('2020-08-13', 'xtb')
    GetColumnNameAndTypeFromTable(query_manager).get_data('xtb')

    sql_query2 = 'select * from xtb'
    SQLQueryExecutor(context).execute_query(sql_query2)


class DeleteDataFromDB:
    pass
