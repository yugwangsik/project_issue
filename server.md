# ubuntu ssh 설치
- sudo apt install openssh-server

# 방화벽해제
- sudo ufw enable
- sudo ufw allow 22
- sudo ufw reload

# ubuntu waiting for cache lock could not get lock /var/lib/dpkg/lock-frontend 에러 해결
  - sudo rm /var/lib/apt/lists/lock
  - sudo rm /var/cache/apt/archives/lock
  - sudo rm /var/lib/dpkg/lock*
  
# E:의존성에 맞지 않습니다. 에러 해결
  - sudo apt --fix-broken install
