## 라즈베리파이 update & upgrade
  - sudo apt-get update
  - sudo apt-get upgrade

## 라즈베리파이 I2C설정
  - sudo raspi-config
  - 3.Interface Options
  - I2C enable
  - sudo reboot
  
## I2C 패키지 설치
  - sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y

## I2C 테스트
  - sudo i2cdetect -y 1

## 라이브러리 설치
  - sudo pip3 install adafruit-circuitpython-ADXL34x
