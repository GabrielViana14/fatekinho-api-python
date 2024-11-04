import pymssql


def get_connection():
    conn = pymssql.connect(
        server='fatekinho-fatec.database.windows.net',
        user='admin1@fatekinho-fatec',
        password='Admin@2024',
        database='fatekinho',
        port='1433'
    )
    return conn
