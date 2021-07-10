## Repository의 GPG key를 더하기
  - curl -sL https://repos.influxdata.com/influxdb.key | sudo apt-key add -
  - echo "deb https://repos.influxdata.com/debian stretch stable" | sudo tee /etc/apt/sources.list.d/influxdb.list

## InfluxDB 설치
  - sudo apt update
  - sudo apt install influxdb

## 프로그램 실행
  - sudo service influxdb start

## influxdb import with python
  - sudo pip install influxdb
