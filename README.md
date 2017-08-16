# Ansible Role: docker-machine

Installs the [docker-machine](https://github.com/docker/machine/) binary.  This
role includes the command completion script for the bash shell.

## Requirements

None.

## Role Variables

Set the `docker-machine` release version.  (See [available versions](https://github.com/docker/machine/releases))

    docker_machine_version: 0.12.2

Install `docker-machine` at this path:

    docker_machine_install_path: /usr/local/bin

## Dependencies

giovtorres.bash-completion

## Example Playbook

    - hosts: servers
      roles:
         - giovtorres.docker-machine

## License

BSD
