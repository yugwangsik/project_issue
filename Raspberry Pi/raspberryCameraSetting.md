# 카메라셋팅
  - sudo raspi-config -> interfacing Options -> Camera -> yes -> reboot
  
# 카메라 연결 확인
  - vcgencmd get_camera
  - supported=1 detected=1 // 정상일때

# 사진 찍기
  - raspistill -o test.jpg
