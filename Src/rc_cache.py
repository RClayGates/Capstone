# imports: std
import os
import pickle
import platform
from time import perf_counter
from datetime import datetime


# imports: non-std
from rc_logger import src_log, cd_up
from rc_files import cache_files

# from rc_virusapi import VT_API_Wrapper

# consts


# main


def main():
    src_log.debug("func enter")
    # vt_file_report(batch_limit=400)
    # vt_report_total_votes()
    # update_cache()
    # with Cache("Cache") as cache:
    #     src_log.debug(len(cache))
    # with Cache("VT_API") as cache:
    #     src_log.debug(len(cache))
    src_log.debug("func exit")
    pass


# code blocks

# TODONE: Error Handling for corrupt pickle
# Traceback (most recent call last):
#   File "<frozen runpy>", line 198, in _run_module_as_main
#   File "<frozen runpy>", line 88, in _run_code
#   File "I:\My Drive\Code\Git\Organized-chaos(bu)\Python\Capstone\Src\__init__.py", line 175, in <module>
#     main()
#   File "I:\My Drive\Code\Git\Organized-chaos(bu)\Python\Capstone\Src\__init__.py", line 26, in main
#     update_cache()
#   File "I:\My Drive\Code\Git\Organized-chaos(bu)\Python\Capstone\Src\__init__.py", line 155, in update_cache
#     with Cache("Cache") as cache:
#   File "I:\My Drive\Code\Git\Organized-chaos(bu)\Python\Capstone\Src\rc_cache.py", line 50, in __enter__
#     self.data = pickle.load(self._filestream)
#                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# EOFError: Ran out of input


class Cache:
    def __init__(self, target_cache) -> None:
        self.filepath = os.path.join(
            (cd_up(cd_up(__file__))),
            ".env",
            platform.uname()[1] + "_" + target_cache + ".pkl",
        )
        if not os.path.exists(os.path.dirname(self.filepath)):
            os.makedirs(os.path.dirname(self.filepath))
        src_log.debug(self.filepath)
        pass

    def __enter__(self) -> dict:
        try:
            self._filestream = open(self.filepath, "rb")
        except FileNotFoundError as _FNFError:
            src_log.exception(_FNFError)
            with open(self.filepath, "xb") as byte_stream:
                pickle.dump({"CreationDate": datetime.now()}, byte_stream)
            self._filestream = open(self.filepath, "rb")
        try:
            self.data = pickle.load(self._filestream)
            self._filestream.close()
            src_log.debug("Data retrieved")
            return self.data
        except EOFError as _EOFError:
            # TODONE: error handle pickle bug
            src_log.error(
                f"{_EOFError = } \n\tCorrupted Local Cache Pickle, must recreate cache"
            )
            self._filestream.close()
            with open(self.filepath, "wb") as byte_stream:
                pickle.dump({"CreationDate": datetime.now()}, byte_stream)
            raise _EOFError
        except Exception as _E:
            src_log.exception(_E.__class__.mro())

    def __exit__(self, exc_type, exc_value, exc_tb):
        with open(self.filepath, "wb") as file_obj:
            pickle.dump(self.data, file_obj)
        src_log.debug("Data stored")


if __name__ == "__main__":
    src_log.debug(f'{"Program Start", datetime.now()}')
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.4f}")
    src_log.debug(datetime.now())
