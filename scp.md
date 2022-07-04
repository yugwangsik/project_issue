## SCP 명령어 단일 파일
  -  scp [옵션] [파일명] [원격지_id]@[원격지_ip]:[받는 위치]
  -  scp testfile2 root@192.168.159.129:/tmp/testclient  


## SCP 명령어 다중 파일
  -  scp [옵션] [파일명 1] [파일명 2] [원격지_id]@[원격지_ip]:[받는 위치]
  -  scp tesfile1 testfile2 root@192.168.159.129:/tmp/testclient


## SCP 명령어 디렉토리
  -  scp [옵션] [디렉터리 이름] [원격지_id]@[원격지_ip]:[보낼 경로]
  -  scp -r testgogo root@192.168.159.129:/tmp/testclient
