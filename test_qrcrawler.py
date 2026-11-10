"""Tests for qrcrawler.py argument handling.

Run with: python -m pytest test_qrcrawler.py -v
"""

import subprocess
import sys
from pathlib import Path

QRCRAWLER = Path(__file__).with_name('qrcrawler.py')


def run_crawler(*args):
    return subprocess.run(
        [sys.executable, str(QRCRAWLER), *args],
        capture_output=True,
        text=True,
        timeout=120,
    )


def test_no_keywords_prints_usage_and_exits_nonzero():
    proc = run_crawler()
    assert proc.returncode != 0
    assert 'usage' in proc.stderr.lower()
    assert 'Traceback' not in proc.stderr
