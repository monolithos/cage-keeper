from cage_keeper.cage_keeper import CageKeeper

RPC_HOST = "https://kovan.infura.io/v3/683836c8b9384898a9f99d483ae389bc"
NETWORK = "kovan"

ETH_FROM = "0xC0CCab7430aEc0C30E76e1dA596263C3bdD82932"
KEY_FILE = "/home/captain/development/dss-deploy-scripts/keystore.json"
PASS_FILE = "/home/captain/development/dss-deploy-scripts/p.pass"

ADDRESSES_FILE = "/home/captain/development/makerdao_python/chief-keeper/addresses/kovan-addresses.json"


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
