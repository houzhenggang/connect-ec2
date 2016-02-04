import pytest
import json
from click.testing import CliRunner
from connect_ec2 import cli


@pytest.fixture
def runner():
    return CliRunner()

def test_cli_with_arg(runner):
    result = runner.invoke(cli.main, ['s-monolith-web-use1d-spto7w'])
    assert result.exit_code == 0
    assert not result.exception
    assert result.output.strip() == 'Connecting to s-monolith-web-use1d-spto7w.'
