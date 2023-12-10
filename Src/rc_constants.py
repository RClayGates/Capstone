# import: std
import os
from datetime import datetime
from time import perf_counter

# import: non-std

from rc_logger import src_log

# const
large_file = r"D:\myvms\70-411Group\411Server1\Snapshots\{305760a7-f57a-4fda-8325-60c371e88f7a}.vdi"
# large_file = 19Gb

# main


def main():
    src_log.debug(sector := pow(2, 9))  # 512
    src_log.debug(size := os.path.getsize(large_file))
    with open(large_file, "rb") as byte_obj:
        for index in range(int(size / sector)):
            byte_stream = byte_obj.read(sector)
            src_log.debug(index)
            src_log.debug(byte_stream)


# code blocks
if __name__ == "__main__":
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.4f}")
    src_log.debug(datetime.now())
