from Trace import Trace
from Finder import Finder


class Builder:
    def __init__(self, trace: Trace):
        self.trace = trace

    def build_trace(self):
        for tr in self.trace.get_trace():
            yield self.build_line(tr)

    @staticmethod
    def build_line(line: list):
        number, domain, ip = line
        return [number, ip, Finder.get_as(ip), Finder.get_country(ip), Finder.get_provider(ip)]

    def print_trace(self):
        for line in self.build_trace():
            if line[1] == " * * * ":
                print("{:^4}| {:^16}| {:^10} | {:^6} | {:^20} |".format(line[0], line[1], "None", "None", "None"))
                print("-" * 68)
                break
            print("{:^4}| {:^16}| {:^10} | {:^6} | {:^20} |".format(*line))
            print("-" * 68)