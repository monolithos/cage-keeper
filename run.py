import os

from cage_keeper.cage_keeper import CageKeeper


BASE_PATH = os.path.dirname(__file__)

NETWORK = "kovan"
# NETWORK = "mainnet"

# ETHEREUM_SETTINGS
if NETWORK.upper() == "KOVAN":
    RPC_HOST = 'https://kovan.infura.io/v3/*****'
    ETH_FROM = '0x0000000000000000000000000000000000000000'
    KEY_FILE = "/PATH/TO/KEY/FILE.json"
    PASS_FILE = "/PATH/TO/PASS/FILE.pass"
    ADDRESSES_FILE = os.path.join(BASE_PATH, 'addresses', 'kovan-addresses.json')  # or '/PATH/TO/ADDRESS/FILE.json'
elif NETWORK.upper() == "MAINNET":
    RPC_HOST = 'https://mainnet.infura.io/v3/*****'
    ETH_FROM = "0x0000000000000000000000000000000000000000"
    KEY_FILE = "/PATH/TO/KEY/FILE.json"
    PASS_FILE = "/PATH/TO/PASS/FILE.pass"
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
