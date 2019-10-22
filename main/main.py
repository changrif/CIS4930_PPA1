from console import console
from api import api
import db
import threading


if __name__ == "__main__":
    t1 = threading.Thread(target=api.run)
    t1.daemon = True
    t1.start()

    console.run()