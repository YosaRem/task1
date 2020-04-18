import re


class IPDomainNameChecker:
    @staticmethod
    def check(address):
        if not (IPDomainNameChecker.check_ip(address) or IPDomainNameChecker.check_domain_name(address)):
            raise Exception("Invalid address")

    @staticmethod
    def check_ip(ip):
        return re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", ip)

    @staticmethod
    def check_domain_name(name):
        return re.match(r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$", name)


class TraceFormatter:
    @staticmethod
    def format_trace(trace):
        for line in trace:
            line = line[3:]
            if len(line) < 1:
                break
            if line[1] == "*":
                break
            splited_line = line.split(" ")
            domain = splited_line[1]
            ip = splited_line[2].strip("(").strip(")")
            yield domain, ip
        yield " * * * ", " * * * "
