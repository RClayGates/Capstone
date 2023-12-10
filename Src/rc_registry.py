# import: std
import os
import winreg as wr
from time import perf_counter
from datetime import datetime as dt_dt, timedelta as dt_td

# import: non-std
from rc_logger import src_log

# const

# main


def main():
    pass


def reg_walk(top="", topdown=True, hives=True, date_string=True):
    """
    Perform similar functionality to os.walk but for the windows
        registry.
    top =           The key that you wish to start the reg_walk at
    hives =         If left True, will iterate through all available registry
                        hives.
    date_string =   If left True, will present date as a string,
                        but if False, will return a datetime.datetime object
    """
    src_log.debug("func enter")
    HKEY_CONST = {
        "HKCC": wr.HKEY_CURRENT_CONFIG,
        "HKCR": wr.HKEY_CLASSES_ROOT,
        "HKCU": wr.HKEY_CURRENT_USER,
        "HKDD": wr.HKEY_DYN_DATA,  # Cannot use QueryInfoKey on
        "HKLM": wr.HKEY_LOCAL_MACHINE,
        "HKPD": wr.HKEY_PERFORMANCE_DATA,
        "HKUR": wr.HKEY_USERS,
    }

    def hive_walk(hive, winreg_HKEY_const, new_top):
        src_log.debug("func enter")
        """
        Recursively travel down each Registry subkey
            generating the following:
                hive =          current hive
                key_name =      current key path
                subkeys =       list of subkeys
                values =        list of tuples of length 3
                        values[0] = string containing value name
                        values[1] = object holding value data, type depend on reg type
                        values[2] = int that identifies type of value data
                            TODO: double check if below is accurate
                            {   0 : REG_BINARY
                                1 : REG_DWORD
                                2 : REG_DWORD_LITTLE_ENDIAN
                                3 : REG_DWORD_BIG_ENDIAN
                                4 : REG_EXPAND_SZ
                                5 : REG_LINK
                                6 : REG_MULTI_SZ
                                7 : REG_NONE
                                8 : REG_QWORD
                                9 : REG_QWORD_LITTLE_ENDIAN
                                10: REG_SZ  }
                date_modified = date the key was last modified
        """
        key_name = new_top
        winreg_HKEY_const = value
        WIN32_EPOCH = dt_dt(1601, 1, 1)
        try:
            key_name = key_name.removeprefix("\\")
            opened_key = wr.OpenKeyEx(winreg_HKEY_const, key_name)
            subkey_count = wr.QueryInfoKey(opened_key)[0]
            value_count = wr.QueryInfoKey(opened_key)[1]
            date_modified_ns = wr.QueryInfoKey(opened_key)[2]
            subkeys = [wr.EnumKey(opened_key, index) for index in range(subkey_count)]
            values = [wr.EnumValue(opened_key, index) for index in range(value_count)]
            wr.CloseKey(opened_key)
            date_modified = WIN32_EPOCH + dt_td(microseconds=date_modified_ns // 10)
            if date_string:
                date_modified = date_modified.strftime(
                    "upDate: %Y-%m-%d Time: %H:%M:%S.%f"
                )
        except PermissionError as _PermissionError:
            src_log.debug(f"\t{_PermissionError=}")
        except WindowsError as _WindowsError:
            src_log.debug(f"\t{_WindowsError=}")
        except Exception as _Exception_0:
            src_log.debug(f"\t{_Exception_0=}")
        if topdown:
            yield (hive, key_name, subkeys, values, date_modified)
        try:
            for key in subkeys:
                key_path = key_name + "\\" + key
                if key_name == key_path:
                    continue
                for recursion in hive_walk(hive, winreg_HKEY_const, key_path):
                    yield recursion
        except PermissionError as _PermissionError:
            src_log.debug(f"\t{_PermissionError=}")
        except UnboundLocalError as _UnboundLocalError:
            src_log.debug(f"\t{_UnboundLocalError=}")
        except Exception as _Exception_1:
            src_log.debug(f"\t{_Exception_1=}")

    if hives:
        for key, value in HKEY_CONST.items():
            if key in ["HKDD", "HKPD"]:
                # OSError: [WinError 120] This function is not supported on this system
                continue
            for registry_keys in hive_walk(key, value, top):
                yield registry_keys
    elif hives in HKEY_CONST.keys():
        for registry_keys in hive_walk(hives, HKEY_CONST[hives], top):
            yield registry_keys


# iterate through key values, determining type
def reg_walk_keys():
    src_log.debug("func enter")
    for hive, key_name, subkeys, values, date_modified in reg_walk():
        # src_log.debug(hive, key_name, subkeys, values, date_modified)
        for value in values:
            src_log.debug(f"{hive, key_name}")
            try:
                src_log.debug(f"{type(value[0]), value[0]}")
                src_log.debug(f"{type(value[1]), value[1]}")
                src_log.debug(f"{type(value[2]), value[2]}")
            except Exception as _Exception:
                src_log.debug(_Exception)
            input()


if __name__ == "__main__":
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.2f}")

# write_buffer = []
# for hive, key_name, subkeys, values, date_modified in reg_walk():
#     # for value in values:
#     #     if 'Description' in value[0]:
#     # if hive in ['HKCU','HKLM']:
#     target_list: tuple[str] = (
#         'mshta', 'if', 'fi', 'elif', 'for', 'while', 'else', 'exec', 'eval', '(')
#     for target in target_list:
#         cond = False
#         if target in key_name.lower():
#             cond = True
#         for key in subkeys:
#             if target in key.lower():
#                 cond = True
#         for value in values:
#             for tuple_item in value:
#                 try:
#                     if target in tuple_item.lower():
#                         cond = True
#                 except:
#                     pass
#         if cond:
#             write_buffer.append(f'\n{hive}>>{key_name}')
#             write_buffer.append('\n\tSUBKEYS:')
#             for key in subkeys:
#                 write_buffer.append(f'\n\t{key}')
#             write_buffer.append('\n\tVALUES:')
#             for value in values:
#                 write_buffer.append(f'\n\t{value}')
# with open('output.txt', 'w') as file_obj:
#     file_obj.write('')
# with open('output.txt', 'a') as file_obj:
#     for line in write_buffer:
#         try:
#             file_obj.write(line)
#         except Exception as _Exception:
#             src_log.debug(_Exception)

# Re-run the program with admin rights


# for items in reg_walk():
#     if 'usb' in items[1]:
#         src_log.debug(items)


# winep=dt_dt(1601,1,1)
# for items in reg_walk(date_string=False):
#     date_modified = items[-1]
#     key_path :str = items[1].lower()
#     path_list :list = key_path.split('\\')
#     condition_list = [
#         'security' in key_path,
#         'recent' in key_path,
#         'mounteddevices' in key_path,
#         'password' in key_path,
#         'run' in key_path,
#         'boot' in key_path,
#         'winlogon' in key_path,
#         'delayload' in key_path,

#     ]
#     if dt_td(100000)>(dt_dt.now()-date_modified) and any(condition_list):
# src_log.debug(items[:2],'\n',dt_dt.now(),'\t',dt_dt.now()-date_modified,'\t',date_modified,'\t',date_modified-winep)
# key_age = dt_dt.now()-date_modified
# src_log.debug(path_list[-2:],'\n',date_modified,'\t',key_age)
# src_log.debug(dt_td(100)>(dt_dt.now()-date))
# keyage = {}
# for items in reg_walk(date_string = False):
#     date : dt_dt = items[-1]
#     age = (dt_dt.now()-date)
#     # src_log.debug(items[1], '\n\t', age)
#     keyage[items[1]] = age.total_seconds()

# import json
# src_log.debug(len(keyage))

# with open('test','w') as file_obj:
#     file_obj.write(json.dumps(keyage))

# import json
# with open('test','r') as file_obj:
#     keyag = json.loads(file_obj.read())
#     for key, value in keyag.items():
#     #     if value < 100:
#         value = dt_dt.fromtimestamp(value)
#         src_log.debug(key, value)
