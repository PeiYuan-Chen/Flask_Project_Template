import unittest
import json
from app import create_app
from app.models import db, Book


class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        # create test table and insert some test case
        self.new_book = {"title": "title4", "author": "author4", "rating": 4}
        db.create_all()
        test_book1 = Book(title="title1", author="author1", rating=1)
        test_book2 = Book(title="title2", author="author2", rating=2)
        test_book3 = Book(title="title3", author="author3", rating=3)
        db.session.add_all([test_book1, test_book2, test_book3])
        db.session.commit()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_paginated_books(self):
        res = self.client.get("/books")
        data = json.loads(res.data)
        books = Book.query.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_books"], 3)
        self.assertEqual(data["books"], [book.serialize for book in books])
