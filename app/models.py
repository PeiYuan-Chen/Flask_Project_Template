from flask_sqlalchemy import SQLAlchemy

# init db
db = SQLAlchemy()


class BaseModel(db.Model):
    __tablename__ = "basetable"
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return f"<{self.__class__.__name__}> {self.id}"

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Insertion error for {self.__class__.__name__} {self.id}: {e}")
            raise

    def update(self):
        try:
            db.session.commit()
        except Exception as e:
            print(f"Update error for {self.__class__.__name__} {self.id}: {e}")
            raise

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"Delete error for {self.__class__.__name__} {self.id}: {e}")
            raise


class Book(BaseModel):
    __tablename__ = "books"

    title = db.Column(db.String())
    author = db.Column(db.String())
    rating = db.Column(db.String())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "rating": self.rating,
        }
