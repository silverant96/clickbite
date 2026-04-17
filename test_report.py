import pytest
import csv
import tempfile
from youtube_report import YoutubeReport


@pytest.fixture
def sample_csv():
    """Создаем временный CSV файл с тестовыми данными"""
    content = [
        ['title', 'ctr', 'retention_rate', 'views'],
        ['Clickbait Video', '20.5', '35', '1000'],
        ['Normal Video', '5.0', '80', '500'],
        ['Sensation!', '18.0', '30', '2000'],
        ['Ok Video', '12.0', '60', '800'],
        ['SHOCK!', '25.0', '20', '3000']
    ]

    with tempfile.NamedTemporaryFile(mode='w', newline='', suffix='.csv', delete=False, encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(content)
        return f.name


def test_clickbait_report(sample_csv):
    """Тест: отчет с кликбейтом должен содержать только видео с CTR > 15 и retention < 40"""
    args = {'files': [sample_csv], 'report': 'clickbait', 'delimiter': ','}
    report = YoutubeReport(args)
    result = report.get_clickbait_report()

    assert 'Clickbait Video' in result
    assert 'Sensation!' in result
    assert 'SHOCK!' in result
    assert 'Normal Video' not in result
    assert 'Ok Video' not in result


def test_clickbait_sorting(sample_csv):
    """Тест: видео должны быть отсортированы по CTR от большего к меньшему"""
    args = {'files': [sample_csv], 'report': 'clickbait', 'delimiter': ','}
    report = YoutubeReport(args)
    result = report.get_clickbait_report()

    shock_pos = result.find('SHOCK!')
    clickbait_pos = result.find('Clickbait Video')

    assert shock_pos < clickbait_pos


def test_other_report(sample_csv):
    """Тест: other отчет должен показывать все данные"""
    args = {'files': [sample_csv], 'report': 'other', 'delimiter': ','}
    report = YoutubeReport(args)
    result = report.get_other_report()

    assert 'Clickbait Video' in result
    assert 'Normal Video' in result
    assert 'Sensation!' in result
    assert 'Ok Video' in result
    assert 'SHOCK!' in result


def test_empty_csv():
    """Тест: пустой CSV файл (только заголовки)"""
    content = [['title', 'ctr', 'retention_rate']]

    with tempfile.NamedTemporaryFile(mode='w', newline='', suffix='.csv', delete=False, encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(content)
        empty_file = f.name

    args = {'files': [empty_file], 'report': 'clickbait', 'delimiter': ','}
    report = YoutubeReport(args)
    result = report.get_clickbait_report()

    assert 'title' in result
    assert 'ctr' in result
    assert 'retention_rate' in result


def test_invalid_data():
    """Тест: некорректные числа должны пропускаться"""
    content = [
        ['title', 'ctr', 'retention_rate'],
        ['Video 1', 'not a number', '35'],
        ['Video 2', '20', 'not a number'],
        ['Video 3', '25', '30']
    ]

    with tempfile.NamedTemporaryFile(mode='w', newline='', suffix='.csv', delete=False, encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(content)
        invalid_file = f.name

    args = {'files': [invalid_file], 'report': 'clickbait', 'delimiter': ','}
    report = YoutubeReport(args)
    result = report.get_clickbait_report()

    assert 'Video 3' in result
    assert 'Video 1' not in result
    assert 'Video 2' not in result