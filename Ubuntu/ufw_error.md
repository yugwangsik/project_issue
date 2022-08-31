## 파이썬 재설치 후 ufw 에러
  - sudo find /usr/lib/ -name "ufw"  <- ufw 위치 찾기
  - 현재 자신의 파이썬 버전 확인       <- 당시 3.9 버전 사용
  - ufw 있는 위치로 이동
  - sudo cp -r ufw /usr/local/lib/python3.9/    <- 자신의 파이썬 버전이 있는 폴더 하위에 ufw 복사
