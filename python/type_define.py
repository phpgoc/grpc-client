from typing import Dict, Callable, Any, Optional


class Method:
    name: str
    method: object
    call: Optional[Callable[[Any], Any]]

    def __init__(self, name: str, method: object):
        self.name = name
        self.method = method
        self.call = None

    def set_runnable(self, fn: Callable[[Any], Any]):
        self.call = fn

    def get_request(self):
        return self.method.input_type

    def get_request_fields(self):
        return self.method.input_type.fields

    def run(self, request: object,host :str) -> object:
        return self.call and self.call(request, host, insecure=True)


class Service:
    name: str
    methods: Dict[str, Method]
    call: object

    def __init__(self, name: str):
        self.name = name
        self.methods = dict()

    def add_method(self, method: Method):
        self.methods[method.name] = method
