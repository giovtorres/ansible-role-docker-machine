import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_docker_machine_install(host):
    f = host.file("/usr/local/bin/docker-machine")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_docker_machine_version(host):
    cmd = host.run("/usr/local/bin/docker-machine version")
    assert cmd.rc == 0
    assert "0.12.2" in cmd.stdout


def test_docker_machine_bash_completion(host):
    f = host.file("/etc/bash_completion.d/docker")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644
