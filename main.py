from utils import parse_args
from youtube_report import YoutubeReport

reports_map = {
    'clickbite': YoutubeReport,
}

args = parse_args()
report_name = args.get('report')

if report_name in reports_map:
    report = reports_map[report_name](args)
    report.print_report()
else:
    print(f"❌ Неизвестный тип отчета: {report_name}")