import pymysql


class Db:
    def __init__(self):
        host = "flask-server-mysql"  # use localhost for non-container running
        user = "root"
        password = "root"
        db = "users_flask"
        self.con = pymysql.connect(host=host, user=user, password=password, db=db,
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def insert_new(self, user_name, login_type):
        self.cur.execute("INSERT INTO `users` (`id`,`username`, `login_type`) VALUES (0 ,%s, %s)",
                         (user_name, login_type))
        self.con.commit()
        return self.cur.lastrowid

    def fetch_records(self):
        self.cur.execute("SELECT * from `users`")
        return self.cur.fetchall()

    def fetch_record(self, id):
        self.cur.execute("SELECT * from `users` where `id`=%s", id)
        return self.cur.fetchone()
