import struct
import sys

fileName = sys.argv[1]

with open(fileName, "rb") as f:
    versionNum = f.read(2)
    print("VersionNum: " + versionNum)

    frame = 0
    while True:
        bytesOut = f.read(4)
        if not bytesOut:
            break

        frame += 1
        print("frame[" + str(frame) + "]")
        print("redGain: " + str(struct.unpack('f', bytesOut)[0]))
        print("greenGain: " + str(struct.unpack('f', f.read(4))[0]))
        print("blueGain: " + str(struct.unpack('f', f.read(4))[0]))
        print("exposureDuration: " + str(struct.unpack('f', f.read(4))[0]))
        print("ISO: " + str(struct.unpack('f', f.read(4))[0]))
