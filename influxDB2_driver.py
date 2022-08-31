from datetime import datetime

from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate a Token from the "Tokens Tab" in the UI
token = "CAIjbOjcqkY2pmxocs8H66wyylfIJeUbQ87vQLMlYY2l1lpJn_ogwLUmmozEUmeMcbxu2G5KzblhLalMS7vExQ=="
org = "c4ae385d9b19a8b4"
bucket = "keti_sw"

client = InfluxDBClient(url="http://keties.iptime.org:8086", token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)

data = "testdata,host=4FL_host1 used_percent=23.4"
write_api.write(bucket, org, data)
