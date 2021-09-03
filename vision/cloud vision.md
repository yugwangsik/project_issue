## cloud vision api를 이용하여 수도미터의 값 추출

## step1. cloud vision의 crop 이용하여 수도미터의 사진 자르기
```

def crop_to_hint(image_file):
    """Crop the image using the hints in the vector list."""
    # [START vision_crop_hints_tutorial_crop_to_hints]
    vects = get_crop_hint(image_file)

    im = Image.open(image_file)
    im2 = im.crop([vects[0].x + 270, vects[0].y + 95,   // vects[0].x 는 사진의 왼쪽을 기준으로 +, vects[0].y 는 사진의 위를 기준으로 + 하여 사진을 자른다.
                  vects[2].x - 375, vects[2].y])        // vects[2].x 는 사진의 오른쪽을 기준으로 -, vects[2].y 는 사진의 아래를 기준으로 - 하여 사진을 자른다.
                                                        // 본인은 사진의 밑부분을 자르게되면 인식하는데 제한사항이 자주 발생하여 자르지않고 vects[2].y를 그대로 사용하였다.
    im2.save('output-crop.jpg', 'JPEG')                 // im2.save(원하는 파일명.jpg, 'JPEG')를 하면 된다.
    print('Saved new image to output-crop.jpg')
    # [END vision_crop_hints_tutorial_crop_to_hints]


```

## step2. cloud vision의 OCR 이용하여 사진의 수도미터의 값을 추출
```
def run_quickstart():
    # [START vision_quickstart]
    import io
    import os

    # Imports the Google Cloud client library
    # [START vision_python_migration_import]
    from google.cloud import vision
    # [END vision_python_migration_import]

    # Instantiates a client
    # [START vision_python_migration_client]
    client = vision.ImageAnnotatorClient()
    # [END vision_python_migration_client]

    # The name of the image file to annotate
    file_name = os.path.abspath('output-crop.jpg')     // crop에서 자른 파일명을 넣어 준다.

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.text_detection(image=image)
    labels = response.text_annotations

    for label in labels:
        print(label.description)
    # [END vision_quickstart]


if __name__ == '__main__':
    run_quickstart()
```

## step3. 추출한 값을 influxdb에 저장한다
```
import sys
import datetime
import threading
from influxdb import InfluxDBClient as influxdb

f = open("result.txt", 'r')
lines = f.readlines()
for result in lines:
    result = result.strip()
f.close()

while True:
    data = [{
        'measurement' : 'watermeter',
        'tags':{
            'tagID' : 1002,
        },
        'fields':{
            'water' : result,
        }
    }]
    client = None
    try:
        client = influxdb('localhost',8086,'root','root','WaterMeter')
    except Exception as e:
        print("Exception " + str(e))
    if client is not None:
        try:
            client.write_points(data)
        except Exception as e:
            print("Exception write " + str(e))
        finally:
            client.close()
```

## step4. 실행
```
  - python cut_test.py 이미지 폴더명/이미지이름.jpg crop     // 이미지를 자르는 과정
  - python vision_api.py > result.txt                       // 이미지에서 추출한 값을 result.txt파일로 저장
  - python influx_water.py                                  // result.txt파일을 열고 한줄을 읽어 온 뒤 '\n'제거 후 influxDB에 값을 저장한다.
  ```
