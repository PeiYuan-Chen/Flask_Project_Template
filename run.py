import sys
from app import create_app


def runserver():
    app = create_app()
    app.run()


def runtest():
    import unittest

    tests = unittest.TestLoader().discover(start_dir="test/unit", pattern="test*.py")
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if not results.wasSuccessful():
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        runtest()
    else:
        runserver()
