# Devops

Staging server: 18.222.232.61 (TBD)

Ssh to the staging server:

```bash
ssh ubuntu@18.222.232.61
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
