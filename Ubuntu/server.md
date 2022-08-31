# ubuntu ssh 설치
- sudo apt install openssh-server

# 방화벽해제
- sudo ufw enable
- sudo ufw allow 22
- sudo ufw delete allow 22 // 22번 규칙 삭제
- sudo ufw reload

# ubuntu waiting for cache lock could not get lock /var/lib/dpkg/lock-frontend 에러 해결
  - sudo rm /var/lib/apt/lists/lock
  - sudo rm /var/cache/apt/archives/lock
  - sudo rm /var/lib/dpkg/lock*
  
# E:의존성에 맞지 않습니다. 에러 해결
  - sudo apt --fix-broken install

# 22번포트 확인하기
  - sudo apt install net-tools
  - netstat -tnlp

# putty 접속 아이디 비번
  - sonooffice
  - tinyos

# grafana 설치(ubuntu)
  - sudo apt-get install adduser libfontconfig1
  - wget https://dl.grafana.com/oss/release/grafana_7.5.2_amd64.deb
  - sudo dpkg -i grafana_7.5.2_amd64.deb
  - sudo service grafana-server start //서비스 시작
  - sudo service grafana-server status //서비스 상태 확인
  - sudo systemctl enable grafana-server.service //서버 재부팅시 자동으로 실행
  - sudo ufw allow 3000 // 3000번 포트 활성화
  - sudo ufw reload
  
# putty 나가기
  - ctrl + d
