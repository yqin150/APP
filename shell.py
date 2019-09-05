import subprocess
import sys
import pytest

def generate_report():
    cmd = "allure generate reports -o html --clean"
    subprocess.call(cmd,shell=True)

pytest.main(["-s","-q", "Testcase","--alluredir=reports"])
generate_report()
