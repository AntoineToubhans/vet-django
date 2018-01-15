# Devops

Staging server: 52.14.42.220 (TBD)

Ssh to the staging server:

```bash
ssh ubuntu@52.14.42.220
```

## Provisionning

### Requirements

* Ansible : `sudo pip install ansible`

To provision staging:

```bash
ansible-playbook -i devops/hosts devops/provision.yml
```

To deploy to staging:

```bash
ansible-playbook -i devops/hosts devops/deploy.yml
```
