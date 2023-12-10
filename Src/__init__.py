# imports: std
import os
import webbrowser
from time import sleep
from time import perf_counter

# imports: non-std

# imports: local
from Pygubu_GUI import rc_gui
from rc_cache import Cache
from rc_logger import src_log
from rc_files import cache_files
from rc_virusapi import VT_API_Wrapper

# const


# main


def main() -> None:
    src_log.debug("func enter")
    #
    # update_vt_cache(batch_limit=400)
    #
    # vt_report_total_votes()
    #
    # src_log.debug(retrieve_local_cache())
    #
    # update_cache()
    #

    gui = rc_gui.CapstoneGuiAppTL_00(
        local_cache=retrieve_local_cache,
        vt_cache=retrieve_vt_cache,
        button_01=filter_filepaths,
        button_02=open_vt_webpage,
        menu_01=update_local_cache,
        menu_02=update_vt_cache,
        menu_03=show_console,
    )
    gui.run()
    src_log.debug("func exit")
    pass


# code blocks
def test():
    for count in range(5):
        sleep(1)
        print(count)


def retrieve_local_cache() -> dict:
    src_log.debug("func enter")
    with Cache("Cache") as cache:
        src_log.debug("func exit")
        return cache


def retrieve_vt_cache() -> dict:
    src_log.debug("func enter")
    with Cache("VT_API") as cache:
        src_log.debug("func exit")
        return cache


def filter_filepaths():
    # TODO: determine if coded into gui, or
    pass


def open_vt_webpage(_target_id):
    src_log.debug("func enter")
    webbrowser.open(r"https://www.virustotal.com/gui/file/" + _target_id)
    pass


def update_local_cache() -> None:
    src_log.debug("func enter")
    with Cache("Cache") as cache:
        cache = cache_files(cache)
    src_log.debug("func exit")


def update_vt_cache(_reset: bool = False, batch_limit: int = 3) -> None:
    """
    Calls VirusTotal for x number of hashes to a max of [batch_limit]
    Caches the results
    """
    src_log.debug("func enter")

    vtapi = VT_API_Wrapper()
    with Cache("Cache") as cache:
        with Cache("VT_API") as vt_cache:
            if _reset:
                vt_cache = {}
            src_log.debug(f"{len(cache) = }")
            batch_count = 0
            for index, key in enumerate(cache.keys()):
                src_log.debug(f"{index = }")
                if key == "CreationDate":
                    continue
                if _reset:
                    vt_cache[key] = vtapi.run_hash(key)
                    batch_count += 1
                elif vt_cache.get(key, None) == None:
                    vt_cache[key] = vtapi.run_hash(key)
                    batch_count += 1
                src_log.debug(f"{batch_count = }")
                src_log.debug(f"{key = }")
                src_log.debug(f"{vt_cache.get(key, False) = }")
                if batch_count == batch_limit:
                    break
    src_log.debug("func exit")
    pass


def show_console() -> None:
    src_log.debug("func enter")

    src_log.debug("func exit")
    pass


# Deprecated: too difficult to insert into gui properly
# def populate_treeview_table(vt_cache, local_cache):
#     if not vt_cache:
#         raise RuntimeError(f'{vt_cache = }')
#     for _key in vt_cache:
#         condition_list = [
#             _key == "CreationDate",
#             len(_key) != 32,  # what we want is the hash that are str()
#             type(vt_cache[_key]) != dict,
#             vt_cache[_key].get("error", None),
#         ]
#         if any(condition_list):
#             yield
#         yield {
#             "parent": "",
#             "index": 0,
#             "values": (
#                 _key,
#                 vt_cache[_key]["data"]["attributes"]["reputation"],
#                 local_cache.get(_key)["filepath"],
#             ),
#             # "tags": "cn",
#         }

# INFORMATIONAL
# def vt_report_total_votes() -> None:
#     """for testing"""
#     src_log.debug("func enter")
#     with Cache("Cache") as lcache:
#         lc = lcache
#     with Cache("VT_API") as cache:
#         for key in cache:
#             if type(cache[key]) == type(dict()):
#                 if cache[key].get("data", False):
#                     src_log.debug(
#                         f"{key}",
#                         f"{lc[key]['filepath']}",
#                         f"{cache[key]['data']['reputation']}",
#                     )
#     src_log.debug("func exit")

# INFORMATIONAL
# def key_mapper(_data: dict, _indent=0) -> None:
#     src_log.debug("func enter")
#     for key in _data.keys():
#         src_log.debug(f"{_indent, key}")
#         if _data.get(key, False):
#             if type(_data[key]) == type(dict()):
#                 key_mapper(_data[key], _indent + 1)
#             else:
#                 src_log.debug(f"{(_indent), _data[key]}")
#                 input()
#     src_log.debug("func exit")

# INFORMATIONAL
# def generate_hashlist() -> list:
#     src_log.debug("func enter")
#     with Cache("Cache") as cache:
#         hashlist = []
#         for key in cache.keys():
#             if key == "CreationDate":
#                 continue
#             hashlist.append(key)
#     src_log.debug("func exit")
#     return hashlist


# TODO: was this important?
# def update_vtapi_cache():
#     with Cache("VT_API") as vt_api:
#         with Cache("Cache") as cache:
#             src_log.debug(len(cache))
#             wrap = VT_API_Wrapper()
#             for key in cache.keys():
#                 src_log.debug(type(cache[key]))


def update_cache() -> None:
    src_log.debug("func enter")
    with Cache("Cache") as cache:
        cache = cache_files(cache)
    src_log.debug("func exit")


def reset_cache() -> None:
    src_log.debug("func enter")
    with Cache("Cache") as cache:
        cache = cache_files(cache, _reset=True)
    src_log.debug("func exit")


if __name__ == "__main__":
    src_log.debug("Program Start")
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.2f}")
