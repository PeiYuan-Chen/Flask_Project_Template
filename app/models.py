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
        except:
            db.session.rollback()
            print(f"{self.__class__.__name__} {self.id} insertion error!")
            raise
        finally:
            db.session.close()

    def update(self):
        try:
            db.session.commit()
        except:
            print(f"{self.__class__.__name__} {self.id} update error!")
            raise
        finally:
            db.session.close()

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except:
            db.session.rollback()
            print(f"{self.__class__.__name__} {self.id} delete error!")
            raise
        finally:
            db.session.close()
