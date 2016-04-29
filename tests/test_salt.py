import subprocess
import shlex
import pytest
from assertions import assert_minion_key_state
from config import SALT_CALL


pytestmark = pytest.mark.usefixtures(
    "master", "minion", "wait_minion_key_cached")


def test_minion_key_cached(env):
    assert_minion_key_state(env, "unaccepted")


def test_minion_key_accepted(env, accept_minion):
    assert_minion_key_state(env, "accepted")


def test_ping_minion(env, minion_ready):
    cmd = shlex.split(SALT_CALL.format(**env))
    cmd.append("test.ping")
    output = subprocess.check_output(cmd, env=env)
    assert [env['HOSTNAME'], 'True'] == [it.strip() for it in output.split(':')]