# ubuntu waiting for cache lock could not get lock /var/lib/dpkg/lock-frontend 에러 해결
  - sudo rm /var/lib/apt/lists/lock
  - sudo rm /var/cache/apt/archives/lock
  - sudo rm /var/lib/dpkg/lock*
  
# E:의존성에 맞지 않습니다. 에러 해결
  - sudo apt --fix-broken install
