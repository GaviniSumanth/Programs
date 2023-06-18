from os import environ as env
from os.path import join, dirname
from server import Server

if __name__ == "__main__":
    try:
        print("Starting app")
        Server()
    except Exception as e:
        print(f"An Error has occured:{e}")
    finally:
        print("Exiting app")
