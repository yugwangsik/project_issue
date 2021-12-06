## ubuntu 터미널 설치

## 접속하는 터미널
  - sudo apt-get install openssh-client

## 접속되는 터미널
  - sudo apt-get install openssh-server
  - sudo ufw enable
  - sudo ufw allow 22
  - sudo ufw reload

## ssh 권한설정
  - sudo vim /etc/ssh/sshd_config
  - PermitRootLogin yes
  - PasswordAuthentication yes
