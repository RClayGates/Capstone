# import: std
import os
import sys
import string
import hashlib
import datetime
from time import perf_counter
from typing import Any, Generator
from concurrent.futures import ThreadPoolExecutor as CFThread
from concurrent.futures import ProcessPoolExecutor as CFProcess
from concurrent.futures import as_completed

# import: non-std

# import: local
from rc_logger import src_log
from rc_tui import cursor_posxy, reset_screen

# const
ABCs = string.ascii_uppercase


# main


def main() -> None:
    pass


# code blocks


class File_Attributes:
    def __init__(self, filepath: str) -> None:
        src_log.debug("func enter")
        self._start = perf_counter()
        self.timestamp: datetime.datetime = datetime.datetime.now()
        self.filepath: str = filepath
        self.modified: datetime.datetime = self._get_last_modified()
        self.hash: hashlib.md5.hexdigest = self._get_md5()
        self.time = perf_counter() - self._start
        src_log.debug(f"{self.filepath = }")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        src_log.debug("func enter")
        return self

    def _get_last_modified(self) -> Any:
        src_log.debug("func enter")
        try:
            stat_obj: os.stat_result = os.stat(self.filepath)
        except FileNotFoundError as _FNFError:
            src_log.error(f"{_FNFError= }")
            return _FNFError
        except OSError as _OSError:
            src_log.error(f"{_OSError= }")
            return _OSError
        except Exception as _Exception:
            src_log.exception(f"{_Exception= }")
        try:
            age = datetime.datetime.fromtimestamp(stat_obj.st_mtime)
        except OSError as _OSError:
            src_log.exception(f"{_OSError= }")
            return _OSError
        src_log.debug(f"{age = }")
        return age

    def _get_md5(self) -> hashlib.md5:
        src_log.debug("func enter")
        sector = pow(2, 9)
        try:
            self.size = os.path.getsize(self.filepath)
            hash_obj = hashlib.md5()
            with open(self.filepath, "rb") as byte_obj:
                for _ in range(int(self.size / sector)):
                    hash_obj.update(byte_obj.read(sector))
            return hash_obj.hexdigest()
        except PermissionError as _PError:
            src_log.exception(f"{_PError= }")
            return _PError
        except OSError as _OSError:
            src_log.exception(f"{_OSError= }")
            return _OSError
        # except MemoryError as _MError:
        #     src_log.exception(f'{_MError= }')
        #     return (os.path.getsize(self.filepath), _MError)


def get_drive_letters() -> list[str]:
    # TODO: Implement a more accurate method of retrieving physical drives
    #   it will iterate locally mapped drives which drastically extends time to cache
    src_log.debug("func enter")
    valid = []
    for letter in ABCs:
        if os.path.exists(f"{letter}:"):
            valid.append(letter)
    valid = ["C"]
    return valid


def drive_walk() -> Generator:
    src_log.debug("func enter")
    drive_letters = get_drive_letters()
    for letter in drive_letters:
        for dirpath, dirnames, filenames in os.walk(f"{letter}:"):
            yield (dirpath, dirnames, filenames)


def cache_files(
    _file_cache: dict,
    _reset: bool = False,
    _threshold: int = 500_000_000,
    _output: bool = False,
) -> dict:
    src_log.debug("func enter")
    if _reset:
        _file_cache = {}
    threaded_results = []
    process_results = []
    err = 0
    with CFProcess(max_workers=os.cpu_count()) as cfprocess:
        with CFThread() as cfthread:
            for index, (dirpath, _, filenames) in enumerate(drive_walk()):
                for file in filenames:
                    filepath: str = os.path.join(dirpath, file)
                    if len(filepath) < 50:
                        filepath = filepath + " " * (60 - len(filepath))
                    # clear_screen()
                    if _reset:
                        try:
                            if os.stat(filepath).st_size > _threshold:
                                # if os.path.getsize(filepath) > _threshold:
                                process_results.append(
                                    cfprocess.submit(File_Attributes(filepath))
                                )
                                src_log.debug(
                                    f"{os.stat(filepath).st_size > _threshold = }"
                                )
                        except OSError as _OSError:
                            src_log.exception(f"{_OSError= }")
                        else:
                            threaded_results.append(
                                cfthread.submit(File_Attributes(filepath))
                            )
                            src_log.debug(
                                f"{os.stat(filepath).st_size > _threshold = }"
                            )
                    elif _file_cache.get(filepath, None) == None:
                        try:
                            if os.path.getsize(filepath) > _threshold:
                                process_results.append(
                                    cfprocess.submit(File_Attributes(filepath))
                                )
                                src_log.debug(
                                    f"{os.stat(filepath).st_size > _threshold = }"
                                )
                        except OSError as _OSError:
                            src_log.exception(f"{_OSError= }")
                        else:
                            threaded_results.append(
                                cfthread.submit(File_Attributes(filepath))
                            )
                            src_log.debug(
                                f"{os.stat(filepath).st_size > _threshold = }"
                            )
                    if _output:
                        output = f"""\
FoldersCached=  {index}
Filepath=       {filepath[:2]}...{filepath[-50:]}-----
NumFilesThrd=   {len(threaded_results)}
NumFilesProc=   {len(process_results)}
"""
                        reset_screen()
                        cursor_posxy(0, 0)
                        sys.stdout.write(output)
            for future in as_completed(process_results):
                result: File_Attributes = future.result()
                src_log.debug(type(future.result()))
                _file_cache[result.hash] = {
                    "date_modified": result.modified,
                    "filepath": result.filepath,
                    "timestamp": result.timestamp,
                    "filename": result.filepath.split(os.sep)[-1],
                }
            for future in as_completed(threaded_results):
                result: File_Attributes = future.result()
                src_log.debug(type(future.result()))
                _file_cache[result.hash] = {
                    "date_modified": result.modified,
                    "filepath": result.filepath,
                    "timestamp": result.timestamp,
                    "filename": result.filepath.split(os.sep)[-1],
                }
    return _file_cache


if __name__ == "__main__":
    src_log.debug(f'{"Program Start", datetime.datetime.now()}')
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.4f}")
    src_log.debug(datetime.datetime.now())
