class Connection:
    def request(self, url: str, method: str, options: dict):
        raise NotImplementedError


class Http:
    """High level class depends on the abstraction (Connection)"""

    def __init__(self, http_connection: Connection):
        self.http_connection = http_connection

    def get(self, url: str, options: dict):
        self.http_connection.request(url, 'GET', options)

    def post(self, url: str, options: dict):
        self.http_connection.request(url, 'POST', options)


class XMLHttpService(Connection):
    def request(self, url: str, method: str, options: dict):
        if method == 'GET':
            print('open')
        elif method == 'POST':
            print('send')


class NodeHttpService(Connection):
    def request(self, url: str, method: str, options: dict):
        pass


class MockHttpService(Connection):
    def request(self, url: str, method: str, options: dict):
        pass
