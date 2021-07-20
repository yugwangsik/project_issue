google cloud vision api를 라즈베리파이에서 사용하려다 에러가 발생

## google-cloud 다운
  -pip install google.cloud

pip로 다운을 했지만 라즈베리파이에서 인식을 못했다.

## 파이썬 버전 확인
  -python --version
  
python 버전 확인 결과 python 2.7버전을 사용중

## 파이썬 버전 변경
  - alias python=python3.7

## 파이썬 버전 변경 후 google 라이브러리 다운
  - pip3 install --upgrade google-api-python-client
  - pip3 install google-cloud
  - pip3 install google-cloud-vision

## google cloud vision api key 등록
  - export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
