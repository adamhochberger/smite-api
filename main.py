from smite_api_wrapper.SmiteApiSessionManager import SmiteApiSessionManager


if __name__ == '__main__':
    manager = SmiteApiSessionManager()
    manager.create_session()
    manager.test_session()
    manager.test_items_api()