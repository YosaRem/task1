import os
from Formatters import IPDomainNameFormatter
from Formatters import TraceFormatter


class Trace:
    command_pattern = "traceroute "

    def __init__(self, address):
        IPDomainNameFormatter.check(address)
        self.address = address
        self.trace = self.get_row_trace()

    def get_row_trace(self):
        trace = os.popen(self.command_pattern + self.address).read()
        return trace.split("\n")

    def print_trace(self):
        for d, i in TraceFormatter.format_trace(self.trace[1:]):
            print(d + " " + i)
