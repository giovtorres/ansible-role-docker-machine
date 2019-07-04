# Ansible Role: docker-machine

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-docker-machine.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-docker-machine)
[![Ansible Role](https://img.shields.io/ansible/role/19936.svg)](https://galaxy.ansible.com/giovtorres/docker-machine/)

Installs the [docker-machine](https://github.com/docker/machine/) binary.  This
role includes the command completion script for the bash shell.

## Requirements

None.

## Role Variables

Set the `docker-machine` release version.  (See [available versions](https://github.com/docker/machine/releases))

    docker_machine_version: 0.16.1

Install `docker-machine` at this path:

    docker_machine_install_path: /usr/local/bin

## Dependencies

giovtorres.bash-completion

## Example Playbook

    - hosts: servers
      roles:
         - giovtorres.bash-completion
         - giovtorres.docker-machine

## License

BSD
