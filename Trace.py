import os
from Formatters import IPDomainNameChecker
from Formatters import TraceFormatter


class Trace:
    command_pattern = "traceroute "

    def __init__(self, address):
        IPDomainNameChecker.check(address)
        self.address = address
        self.trace = self.get_row_trace()

    def get_row_trace(self):
        trace = os.popen(self.command_pattern + self.address).read()
        return trace.split("\n")

    def get_trace(self):
        i = 1
        for dom, ip in TraceFormatter.format_trace(self.trace[2:]):
            yield [i, dom, ip]
            i += 1
