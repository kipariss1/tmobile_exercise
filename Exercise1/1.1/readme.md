# Exercise 1.1 – 

## Prerequisites

Runns on ubuntu only

```bash
# Install deps & run
sudo apt update
sudo apt install -y ansible
ansible-playbook -i "localhost," -c local site.yml --ask-become-pass
```