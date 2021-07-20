from sqlalchemy import Column, String

from . import BASE, SESSION


class Broadcast(BASE):
    __tablename__ = "Broadcast"
    chat_id = Column(String(14), primary_key=True)

    def __init__(self, chat_id):
        self.chat_id = chat_id


Broadcast.__table__.create(checkfirst=True)


def add_chnnl_in_db(chat_id: int):
    chnnl_id = Broadcast(str(chat_id))
    SESSION.add(chnnl_id)
    SESSION.commit()


def get_all_chnnl():
    stark = SESSION.query(Broadcast).all()
    SESSION.close()
    return stark


def already_added(chat_id):
    try:
        return SESSION.query(Broadcast).filter(Broadcast.chat_id == str(chat_id)).one()
    except:
        return None
    finally:
        SESSION.close()


def rm_channel(chat_id):
    remove = SESSION.query(Broadcast).get(str(chat_id))
    if remove:
        SESSION.delete(remove)
        SESSION.commit()
