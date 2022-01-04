"""The Dependency Inversion Principle (DIP)

Abstractions should not depend on details. Details should depend on abstraction.
High-level modules should not depend on low-level modules. Both should depend on abstractions
"""


class XMLHttpService:
    def request(self, url, method):
        pass


class Http:
    def __init__(self, xml_http_service: XMLHttpService):
        # bad because XML is the real implementation, but HTTP is a high level class which should not depend
        # on the implementation but on abstractions
        self.xml_http_service = xml_http_service

    def get(self, url: str, options: dict):
        self.xml_http_service.request(url, 'GET')

    def post(self, url: str, options: dict):
        self.xml_http_service.request(url, 'POST')
