from __future__ import print_function
import grpc
import grpc.experimental

import logging
import os
from typing import Dict, Union

from type_define import Method, Service


class NoCodeGen:
    file_path: str
    services: Dict[str, Service]
    protos : object

    def __init__(self, file_path: str):
        self.file_path = os.path.join(Client.PROTOS_DIR, file_path)
        self.services = dict()
        print(f"Loading proto file: {self.file_path}")
        try:
            self.protos = grpc.protos(self.file_path)
        except Exception as e:
            print(f"Error loading proto file: {e}")
            raise
        services = grpc.services(self.file_path)
        self.__reflect_proto()
        self.__reflect_services(services)

    def run(self, service: str, method: str, request: object):
        response = self.services[service].methods[method].run(request, Client.host)
        print(f"Greeter client received: {response}")

    def __reflect_proto(self) -> Union[None,NotImplementedError]:
        for proto in dir(self.protos):
            if proto == "DESCRIPTOR":
                services_by_name = getattr(self.protos, proto).services_by_name
                for service_name, service in services_by_name.items():
                    print(f"Service: {service_name}")
                    self.services[service_name] = Service(service_name)

                    for method in service.methods:
                        if method.client_streaming or method.server_streaming:
                            raise NotImplementedError("Client or server streaming is not supported")
                        print(f"    Request: {method.name}")
                        print(f"    Method Obj1: {method}")

                        type_define_method = Method(method.name, method)
                        self.services[service_name].add_method(type_define_method)


    def __reflect_services(self, services_obj: object):
        services = [attr for attr in dir(services_obj) if attr[0].isupper()]
        for service in services:
            if service in ["EXPECTED_ERROR_RELEASE", "GRPC_GENERATED_VERSION", "GRPC_VERSION", "GreeterStub",
                           "SCHEDULED_RELEASE_DATE"]:
                continue
            if "Service" in service:
                continue

            service_obj = getattr(services_obj, service)
            print(f"Service: {service}")
            methods = [method for method in dir(service_obj) if
                       method[0].isupper() and callable(getattr(service_obj, method))]
            for method in methods:
                print(f"  Method: {method}")

                method_obj = getattr(service_obj, method)
                print(f"    Method Obj2: {method_obj}")
                self.services[service].methods[method].set_runnable(method_obj)



class Client:
    host: str = "localhost:50051"
    PROTOS_DIR: str = "protos"

    @staticmethod
    def set_host(host: str):  # type: ignore
        Client.host = host


if __name__ == "__main__":
    logging.basicConfig()
    print(Client.PROTOS_DIR)
    n = NoCodeGen("helloworld.proto")
    n.run("Greeter", "SayHello", n.protos.HelloRequest(name="yo123u"))