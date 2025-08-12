from algopy import ARC4Contract, String, Map
from algopy.arc4 import abimethod


class PoapContract(ARC4Contract):
    def __init__(self):
        super().__init__()
        # Storage mapping: address -> certificate info string
        self.certificates = Map(key_type=String, value_type=String)

    @abimethod()
    def hello(self, name: String) -> String:
        return "Hello, " + name

    @abimethod()
    def mint_certificate(self, addr: String, cert_data: String) -> None:
        # Save the certificate data for the given address
        self.certificates[addr] = cert_data

    @abimethod()
    def has_certificate(self, addr: String) -> bool:
        return addr in self.certificates

    @abimethod()
    def get_certificate(self, addr: String) -> String:
        if addr in self.certificates:
            return self.certificates[addr]
        else:
            return "No certificate found."

    @abimethod()
    def delete_certificate(self, addr: String) -> None:
        if addr in self.certificates:
            del self.certificates[addr]
