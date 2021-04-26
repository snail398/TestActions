import yadisk
import sys

print(sys.argv[1])
y = yadisk.YaDisk(token="AQAAAAAFzz4bAAcWVJNhoT1G1E81liY-xuEtyr0")
y.mkdir("/Hello Word") # Создать папку
y.upload(sys.argv[1], "/Hello Word/" + sys.argv[1]) # Загружает первый файл