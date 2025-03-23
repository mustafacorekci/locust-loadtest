import os
import datetime
import shutil
from bs4 import BeautifulSoup


class ReportGenerator:
    def __init__(self, reports_dir="reports/"):
        self.reports_dir = reports_dir
        os.makedirs(reports_dir, exist_ok=True)

    def save_report(self, source_file="report.html"):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        destination_file = os.path.join(self.reports_dir, f"report_{timestamp}.html")
        shutil.copyfile(source_file, destination_file)
        print(f"Rapor kaydedildi: {destination_file}")

    def parse_report(self, report_file):
        with open(report_file, 'r') as file:
            soup = BeautifulSoup(file, 'html.parser')

        # Toplam istek sayısını alalım
        total_requests = soup.find("div", {"id": "total_rps"}).text.strip()
        return total_requests
