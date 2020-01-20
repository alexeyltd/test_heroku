class Database:
    def __init__(self, db_name):
        import sqlite3
        self._conn = sqlite3.connect(db_name, check_same_thread=False)
        # import psycopg2
        # self.conn = psycopg2.connect(dbname='d3c4f6ktqnvqk4', user='smxepsaktjhqtj',
        #                              password='9b45654c8f0f89416058dfe82d9c9a6797780f03297661d1d4856de74fa9ded7',
        #                              host='ec2-54-75-238-138.eu-west-1.compute.amazonaws.com',
        #                              port=5432)

        self._cursor = self._conn.cursor()
        self.User = User(self._cursor, self._conn)


class User:
    def __init__(self, cursor, conn):
        self._cursor = cursor
        self._conn = conn

