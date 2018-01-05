# Devops

Staging server: XX.XX.XX.XX (TBD)

Ssh to the staging server:

```bash
ssh ubuntu@XX.XX.XX.XX
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
