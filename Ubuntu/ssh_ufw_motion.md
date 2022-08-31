# ubuntu ssh 설치
- sudo apt install openssh-server

# 방화벽해제
- sudo ufw enable
- sudo ufw allow 22
- sudo ufw reload

# motion 캡쳐 설정
- 75 threshold_tune on
- 87 event_gap 20 // 테스트하면서 조정
- 113 picture_output first
