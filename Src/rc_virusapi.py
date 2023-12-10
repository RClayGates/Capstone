# imports: std
import os
import sys
import time
from time import perf_counter

# imports: non-std
import requests

# imports: local
from rc_logger import src_log

# constants
RATE_LIMIT = 20


def main():
    vtapi = VT_API_Wrapper()
    # example malicious hash: 8d3f68b16f0710f858d8c1d2c699260e6f43161a5510abb0e7ba567bd72c965b
    output = vtapi.run_hash(
        "8d3f68b16f0710f858d8c1d2c699260e6f43161a5510abb0e7ba567bd72c965b"
    )
    print(output["data"]["attributes"]["total_votes"])
    print(output)
    pass


class VT_API_Wrapper:
    def __init__(self) -> None:
        src_log.debug("func enter")
        self.api_path = os.path.join(
            (self.cd_up(self.cd_up(__file__))), ".env", "env.txt"
        )
        self.encoding = sys.getfilesystemencoding()
        self.base_url = "https://www.virustotal.com/api/v3/"
        self.api_key = self.__api_key()
        self.headers = {"x-apikey": self.api_key}

    def cd_up(self, path):
        return os.path.dirname(path)

    def __api_key(self):
        # TODO: Need user interface for properly entering the API key
        #       Also give user the option to change/re-enter API key
        src_log.debug("func enter")
        if not os.path.exists(self.api_path):
            os.makedirs(os.path.dirname(self.api_path))
            with open(self.api_path, "w") as file_obj:
                mem_key = bytes(
                    input("Please enter your VirusTotal API key: "), self.encoding
                )
                key = memoryview(mem_key).hex()
                file_obj.write(key)

        with open(self.api_path, "r") as api:
            api = bytes.fromhex(api.read()).decode(self.encoding)
        src_log.debug("API key retrieved")
        return api

    def run_report(self, _hashlist: list):
        src_log.debug("func enter")
        for hash in _hashlist:
            self.__request_get(hash)

    def run_hash(self, _hash):
        src_log.debug("func enter")
        return self.__request_get(_hash)

    def __request_get(self, _hash):
        src_log.debug("func enter")
        for _ in range(RATE_LIMIT):
            time.sleep(1)
        else:
            src_log.debug(f"{_hash}")
        url = self.base_url + f"files/{_hash}"
        json_response = requests.get(url, headers=self.headers).json()
        return json_response


if __name__ == "__main__":
    start = perf_counter()
    os.chdir(os.path.dirname(__file__))
    main()
    src_log.debug(f"Program Time= {perf_counter() - start:.4f}")
