import sqlalchemy
from .db_session import SqlAlchemyBase


class Battle(SqlAlchemyBase):
    __tablename__ = 'battle'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    preview_img = sqlalchemy.Column(sqlalchemy.String)

    text = sqlalchemy.Column(sqlalchemy.String)
    text_img_1 = sqlalchemy.Column(sqlalchemy.String)
    text_img_2 = sqlalchemy.Column(sqlalchemy.String)
    text_img_3 = sqlalchemy.Column(sqlalchemy.String)
    text_img_4 = sqlalchemy.Column(sqlalchemy.String)
    text_img_5 = sqlalchemy.Column(sqlalchemy.String)
    text_img_6 = sqlalchemy.Column(sqlalchemy.String)
    text_img_7 = sqlalchemy.Column(sqlalchemy.String)

    articles_1 = sqlalchemy.Column(sqlalchemy.String)
    articles_img_1 = sqlalchemy.Column(sqlalchemy.String)

    articles_2 = sqlalchemy.Column(sqlalchemy.String)
    articles_img_2 = sqlalchemy.Column(sqlalchemy.String)

    articles_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    articles_img_3 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    articles_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    articles_img_4 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    articles_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    articles_img_5 = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    video_1 = sqlalchemy.Column(sqlalchemy.String)

    video_2 = sqlalchemy.Column(sqlalchemy.String)

    video_3 = sqlalchemy.Column(sqlalchemy.String)
