import tarfile
import io
import sys
import time

mcdonalds_io = io.BytesIO()
mcdonalds_info = tarfile.TarInfo()

with open("mcdonalds.png", "rb") as mcdonalds:
    mcdonalds_data = mcdonalds.read()
    mcdonalds_info.size = len(mcdonalds_data)
    print(f"1 MCDONALD'S! = {len(mcdonalds_data)} bytes")
    mcdonalds_io.write(mcdonalds_data)

lastprint = 0
x = 0

def bytestats(total: int):
    b = mcdonalds_info.size * total

    return "MCDONALD'S!: {total}; bytes: {bytes}; kb: {kilos}; mb: {megas}".format(
        bytes=b,
        kilos=b/1024,
        megas=b/1024/1024
    )

with tarfile.open("/dev/st0", "w") as tar:
    try:
        while True:
            mcdonalds_io.seek(0)
            mcdonalds_info.name = f"mcdonalds/mcdonalds-{x}.png"
            tar.addfile(
                tarinfo=mcdonalds_info,
                fileobj=mcdonalds_io
            )
            # 10 updates per sec
            if time.time() > (lastprint + 0.1):
                sys.stdout.write("\r\u001b[1000D" + bytestats(x))
                lastprint = time.time()
            x += 1
    except KeyboardInterrupt:
        tar.close()