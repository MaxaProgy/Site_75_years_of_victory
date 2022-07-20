from main import db


class Battle(db.Model):
    __tablename__ = 'battle'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)

    preview_img = db.Column(db.String)

    text = db.Column(db.String)
    text_img_1 = db.Column(db.String)
    text_img_2 = db.Column(db.String)
    text_img_3 = db.Column(db.String)
    text_img_4 = db.Column(db.String)
    text_img_5 = db.Column(db.String)
    text_img_6 = db.Column(db.String)
    text_img_7 = db.Column(db.String)

    articles_1 = db.Column(db.String)
    articles_img_1 = db.Column(db.String)

    articles_2 = db.Column(db.String)
    articles_img_2 = db.Column(db.String)

    articles_3 = db.Column(db.String, nullable=True)
    articles_img_3 = db.Column(db.String, nullable=True)

    articles_4 = db.Column(db.String, nullable=True)
    articles_img_4 = db.Column(db.String, nullable=True)

    articles_5 = db.Column(db.String, nullable=True)
    articles_img_5 = db.Column(db.String, nullable=True)

    video_1 = db.Column(db.String)

    video_2 = db.Column(db.String)

    video_3 = db.Column(db.String)
