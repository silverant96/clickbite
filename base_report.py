import csv

class CSVReportReader:
    def __init__(self, args):
        self.args = args
        self.data = []  # таблица с данными
        self.headers = []
        self._read_files()

    def _read_files(self):
        """Чтение всех файлов из списка"""
        files = self.args.get('files', [])

        for file in files:
            try:
                with open(file, 'r', encoding='utf-8') as f:
                    reader = csv.reader(f, delimiter=self.args.get('delimiter', ','))
                    rows = list(reader)

                    if rows:
                        if not self.headers:
                            self.headers = rows[0]
                            self.data.extend(rows[1:])
                        else:
                            self.data.extend(rows[1:] if len(rows) > 1 else [])
            except FileNotFoundError:
                print(f"❌ Файл не найден: {file}")
