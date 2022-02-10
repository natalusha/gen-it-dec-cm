import mysql.connector as mysql


class my_sql_context_manager:
    def __init__(self, hostname, user, password, db_name):
        self.hostname = hostname
        self.user = user
        self.password = password
        self.db_name = db_name
        self.db = None
        self.cursor = None

    def __enter__(self):
        self.db = mysql.connect(
            host=self.hostname,
            user=self.user,
            password=self.password,
            database=self.db_name,
        )
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.cursor.close()
        self.db.close()
