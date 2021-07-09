## repository의 GPG key를 더한다
  - curl https://bintray.com/user/downloadSubjectPublickey?username=bintray | sudo apt-key add -
  - echo "deb https://dl.bintray.com/fg2it/deb stretch main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
  
## 프로그램 설치
  - sudo apt update
  - sudo apt install grafana

## 프로그램 실행
  - 
