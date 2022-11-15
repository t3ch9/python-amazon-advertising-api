
from ..client import Client


class Reports(Client):

    def request_report(self, record_type, data):
        self.uri_path = "/v2/sp/{}/report".format(record_type)
        self.method = "post"
        self.data = data
        return self.execute()

    def get_report(self, report_id):
        self.uri_path = "/v2/reports/{}".format(report_id)
        self.method = "get"
        return self.execute()

    def get_report_download_url(self, location):
        self.method = "get"
        return self.execute_download(location)

    def get_report_download(self, report_id):
        self.uri_path = "/v2/reports/{}/download".format(report_id)
        self.method = "get"
        self.headers.pop("Content-Type")
        self.headers["Accept-encoding"] = "gzip"
        return self.execute()


class Reporting(Client):

    def create_reports(self, data):
        self.method = "post"
        self.uri_path = "/reporting/reports"
        self.data = data
        return self.execute()

    def get_reports(self, report_id):
        self.method = "get"
        self.uri_path = "/reporting/reports/{}".format(report_id)
        return self.execute()

    def delete_reports(self, report_id):
        self.method = "delete"
        self.uri_path = "/reporting/reports/{}".format(report_id)
        return self.execute()
