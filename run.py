import os

from cage_keeper.cage_keeper import CageKeeper


BASE_PATH = os.path.dirname(__file__)

NETWORK = "kovan"
# NETWORK = "mainnet"

# ETHEREUM_SETTINGS
if NETWORK.upper() == "KOVAN":
    RPC_HOST = 'https://kovan.infura.io/v3/683836c8b9384898a9f99d483ae389bc'
    ETH_FROM = '0xC0CCab7430aEc0C30E76e1dA596263C3bdD82932'
    KEY_FILE = "/home/captain/development/keystore/9ae_keystore.json"
    PASS_FILE = "/home/captain/development/keystore/9ae_pass.pass"
    ADDRESSES_FILE = os.path.join(BASE_PATH, 'addresses', 'kovan-addresses.json')  # or '/PATH/TO/ADDRESS/FILE.json'
elif NETWORK.upper() == "MAINNET":
    RPC_HOST = 'https://mainnet.infura.io/v3/683836c8b9384898a9f99d483ae389bc'
    ETH_FROM = "0xDb7A67fb3a6135c9d5167675ca8560B4bCAee912"
    KEY_FILE = "/home/captain/development/keystore/912_keystore.json"
    PASS_FILE = "/home/captain/development/keystore/912_pass.pass"
    ADDRESSES_FILE = os.path.join(BASE_PATH, 'addresses', 'mainnet-addresses.json')  # or '/PATH/TO/ADDRESS/FILE.json'
else:
    raise Exception('NOT SUPPORTED NETWORK')


if __name__ == '__main__':
    cage_args = [
        '--rpc-host', RPC_HOST,
        '--eth-from', ETH_FROM,
        '--eth-key', f'key_file={KEY_FILE},pass_file={PASS_FILE}',
        '--dss-deployment-file', ADDRESSES_FILE,
        '--network', NETWORK,
        '--max-errors', '100',
        '--vat-deployment-block', '17707858',
        # '--previous-cage',
        # '--debug',
    ]
    CageKeeper(cage_args).main()
