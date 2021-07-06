# 와이파이설정
  - 설정 -> Preferences -> Raspberry Pi Configuration -> Localisation -> Wireless LAN Country -> GB Britain (UK)

# 키보드(영문)설정
  - 설정 -> Preferences -> Raspberry Pi Configuration -> Localisation -> Keyboard -> Layout, variand -> English(US)

# 무선랜 설정파일
  - vim /etc/wpa_supplicant/wpa_supplicant.conf

# 무선랜 끊기면 5분후에 자동연결
  - sudo vim /usr/local/bin/wifi_rebooter.sh // 스크립트 파일 생성
```
SERVER=8.8.8.8
ping -c2 ${SERVER} > /dev/null  // 핑을 보내서 wifi연결 상태 확인
if [ $? != 0 ]                  // 핑에서 return값을 확인하여 보내졌는지 확인
then
    sudo ifconfig wlan0 down        // wlan0 연결을 끊기
    sudo ifconfig wlan0 up          // wlan0 다시 연결
fi 
```
