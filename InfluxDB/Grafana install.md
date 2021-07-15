## repository의 GPG key를 더한다
  - wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
  - echo "deb https://packages.grafana.com/oss/deb stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list
  
## 프로그램 설치
  - sudo apt-get update
  - sudo apt install grafana

## 프로그램 실행
  - sudo service grafana-server start
