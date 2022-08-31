## 파이썬 버전 확인
  -python --version
  
python 버전 확인 결과 python 2.7버전을 사용 중
사용하려면 python 3.x 버전에서 사용 가능

## 파이썬 버전 변경
  - alias python=python3.7

## 파이썬 버전 변경 후 google 라이브러리 다운
  - pip3 install --upgrade google-api-python-client
  - pip3 install google-cloud
  - pip3 install google-cloud-vision

## ModuleNotFoundError: No module named 'google'
  - pip3 install --upgrade google-cloud-storage

## ImportError: cannot import name 'texttospeech' from 'google.cloud'
  - pip3 install google-cloud-texttospeech

## google cloud vision api key 등록
  - $ sudo vim .bashrc
  - export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your/credentials-key.json
