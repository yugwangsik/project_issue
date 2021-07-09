## ubuntu bit 확인
  - getconf LONG_BIT

## java 폴더 생성 및 환경변수 설정
  - sudo mkdir -p /usr/local/java
  - 파일질라로 tar.gz파일 넘기기
  - sudo mv jdk-8u191-linux-x64.tar.gz /usr/local/java/      // tar.gz 파일 옮기기
  - cd /usr/local/java -> sudo tar xvfz /usr/local/java/jdk-xxxxx-linux-x64.tar.gz   // 다운받은 버전에 맞게 이름설정

## /etc/profile 설정
  - sudo vim /etc/profile
  - 맨 아래에 입력
  ```
  export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")
  sudo update-alternatives --install "/usr/bin/java" "java" "/usr/local/java/jdkx.x.x_xxx/bin/java" 1;
  sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/local/java/jdkx.x.x_xxx/bin/javac" 1;
  sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/local/java/jdkx.x.x_xxx/bin/javaws" 1;
  sudo update-alternatives --install "/usr/bin/jar" "jar" "/usr/local/java/jdkx.x.x_xxx/bin/jar" 1;
  sudo update-alternatives --set java /usr/local/java/jdkx.x.x_xxx/bin/java;
  sudo update-alternatives --set javac /usr/local/java/jdkx.x.x_xxx/bin/javac;
  sudo update-alternatives --set javaws /usr/local/java/jdkx.x.x_xxx/bin/javaws;
  sudo update-alternatives --set jar /usr/local/java/jdkx.x.x_xxx/bin/jar;
  ```
  - . /etc/profile     // profile 설정 반영
  - java -version      // 확인
