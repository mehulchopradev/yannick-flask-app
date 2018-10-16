from mysql.connector import MySQLConnection
from configparser import ConfigParser

def connect():
    # parameters from the ini file
    cp = ConfigParser()
    cp.read('/home/mehul/Documents/training/python/yannick-flask-app/dbconnect.ini')
    paramsmap = {}

    if cp.has_section('mysql'):
        items = cp.items('mysql')
        for item in items:
            paramsmap[item[0]] = item[1]

        con = MySQLConnection(**paramsmap)
        return con
    else:
        raise Exception('Check format of config file')
