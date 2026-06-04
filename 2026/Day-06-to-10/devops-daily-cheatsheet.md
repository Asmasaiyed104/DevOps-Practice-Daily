# Linux + DevOps Simple Notes

## Connect to AWS Server

```bash
cd .ssh/

ssh -i "linux-practice.pem" ubuntu@your-ec2-ip
```

---

# Navigation Commands

## Show files

```bash
ls
```

## Show hidden files

```bash
ls -a
```

## Detailed list

```bash
ls -l
```

## Go inside folder

```bash
cd devops/
```

## Go back

```bash
cd ..
```

## Go home

```bash
cd ~
```

## Current location

```bash
pwd
```

---

# File Commands

## Create file

```bash
touch notes.txt
```

## Write text

```bash
echo "Linux is powerful"
```

## Save text into file

```bash
echo "Linux is powerful" >> notes.txt
```

## Read file

```bash
cat notes.txt
```

## First lines

```bash
head -n 2 notes.txt
```

## Last lines

```bash
tail -n 2 notes.txt
```

---

# Important Linux Folders

## Var folder

```bash
cd /var
```

## Temp folder

```bash
cd /tmp
```

## Home folder

```bash
cd /home
```

## Bin folder

```bash
ls -l /bin
```

---

# Docker Commands

## Install Docker

```bash
sudo apt install docker.io -y
```

## Start Docker

```bash
sudo systemctl start docker
```

## Enable Docker

```bash
sudo systemctl enable docker
```

## Docker status

```bash
sudo systemctl status docker
```

## Docker version

```bash
docker --version
```

## Test Docker

```bash
sudo docker run hello-world
```

## Running containers

```bash
docker ps
```

## Fix Docker permission

```bash
sudo usermod -aG docker ubuntu
```

## Refresh group

```bash
newgrp docker
```

---

# Nginx Commands

## Install nginx

```bash
sudo apt install nginx -y
```

## Start nginx

```bash
sudo systemctl start nginx
```

## Enable nginx

```bash
sudo systemctl enable nginx
```

## Check nginx

```bash
sudo systemctl status nginx
```

---

# Service Commands

## List services

```bash
systemctl list-units
```

## Show logs

```bash
journalctl -u docker -n 50
```

## Live logs

```bash
journalctl -u docker -f
```

---

# User Commands

## Create user

```bash
sudo useradd -m tokyo
```

## Set password

```bash
sudo passwd tokyo
```

## View users

```bash
cat /etc/passwd
```

## Search user

```bash
cat /etc/passwd | grep tokyo
```

---

# Group Commands

## Create group

```bash
sudo groupadd developers
```

## Add user to group

```bash
sudo usermod -aG developers tokyo
```

## Check groups

```bash
groups tokyo
```

## View groups

```bash
cat /etc/group
```

---

# Permission Commands

## Change permission

```bash
chmod 777 script.sh
```

## Read and write only

```bash
chmod 660 script.sh
```

## Make executable

```bash
chmod +x script.sh
```

---

# Ownership Commands

## Change owner

```bash
sudo chown ubuntu script.sh
```

## Change group

```bash
sudo chgrp developers script.sh
```

---

# Project Folder Commands

## Create project folder

```bash
sudo mkdir -p /opt/dev-project
```

## Change group

```bash
sudo chgrp developers /opt/dev-project
```

## Give permission

```bash
sudo chmod 775 /opt/dev-project
```

---

# Script Commands

## Create script

```bash
vim script.sh
```

## Run script

```bash
./script.sh
```

## Read only mode

```bash
vim -R script.sh
```

---

# Helpful Commands

## Update packages

```bash
sudo apt update
```

## Install package

```bash
sudo apt install package-name -y
```

## Check memory

```bash
free -h
```

## Check disk space

```bash
df -h
```

## Running processes

```bash
top
```

## Exit server

```bash
exit
```

---

# Quick Meanings

| Command    | Meaning           |
| ---------- | ----------------- |
| ls         | show files        |
| cd         | change folder     |
| pwd        | current location  |
| cat        | read file         |
| touch      | create file       |
| mkdir      | create folder     |
| chmod      | change permission |
| chown      | change owner      |
| systemctl  | manage services   |
| docker ps  | show containers   |
| journalctl | show logs         |
