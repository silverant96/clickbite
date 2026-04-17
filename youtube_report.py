from base_report import CSVReportReader
from tabulate import tabulate


class YoutubeReport(CSVReportReader):

    def get_report(self):
        report_types = {
            'clickbait': self.get_clickbait_report,
            'other': self.get_other_report
        }

        report_name = self.args.get('report')

        if report_name in report_types:
            return report_types[report_name]()
        else:
            print(f"❌ Неизвестный тип отчета: {report_name}")

    def get_clickbait_report(self):
        filtered_data = []
        headers_indices = {header: idx for idx, header in enumerate(self.headers)}
        header_ctr = headers_indices['ctr']
        header_retention_rate = headers_indices['retention_rate']
        for row in self.data:
            try:
                ctr = float(row[header_ctr])
                retention = float(row[header_retention_rate])

                if ctr > 15 and retention < 40:
                    filtered_row = [
                        row[headers_indices['title']],
                        row[headers_indices['ctr']],
                        row[headers_indices['retention_rate']]
                    ]
                    filtered_data.append(filtered_row)
            except (ValueError, KeyError):
                continue

        filtered_data.sort(key=lambda x: x[1], reverse=True)
        filtered_headers = ['title', 'ctr', 'retention_rate']
        return tabulate(filtered_data, headers=filtered_headers, tablefmt="fancy_grid")

    def get_other_report(self):
        return tabulate(self.data, headers=self.headers, tablefmt="grid")