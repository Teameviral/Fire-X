from sqlalchemy import Column, String, UnicodeText

from firebot.modules.sql_helper import BASE, SESSION


class Gban(BASE):
    __tablename__ = "gban"
    user_id = Column(String(14), primary_key=True)
    reason = Column(UnicodeText)

    def __init__(self, user_id, reason):
        self.user_id = user_id
        self.reason = reason


Gban.__table__.create(checkfirst=True)


def gban_user(user_id: int, reason):
    gbanner = Gban(str(user_id), reason)
    SESSION.add(gbanner)
    SESSION.commit()


def gban_data(user_id: int):
    try:
        s__ = SESSION.query(Gban).get(str(user_id))
        return int(s__.user_id), s__.reason
    finally:
        SESSION.close()


def is_gbanned(user_id: int):
    try:
        s__ = SESSION.query(Gban).get(str(user_id))
        if s__:
            return s__.reason
    finally:
        SESSION.close()


def ungban_user(user_id):
    ungbanner = SESSION.query(Gban).get(str(user_id))
    if ungbanner:
        SESSION.delete(ungbanner)
        SESSION.commit()
