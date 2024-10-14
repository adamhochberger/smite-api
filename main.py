from smite1_api_wrapper.Smite1ApiSessionManager import Smite1ApiSessionManager


if __name__ == '__main__':
    manager = Smite1ApiSessionManager()
    manager.create_session()
    manager.test_session()
    manager.test_items_api()