from cage_keeper.cage_keeper import CageKeeper


if __name__ == '__main__':
    cage_args = [
        '--rpc-host', 'https://kovan.infura.io/v3/683836c8b9384898a9f99d483ae389bc',
        '--eth-from', '0xC0CCab7430aEc0C30E76e1dA596263C3bdD82932',
        '--eth-key', 'key_file=/home/captain/development/dss-deploy-scripts/keystore.json,pass_file=/home/captain/development/dss-deploy-scripts/p.pass',
        '--dss-deployment-file', '/home/captain/development/makerdao_python/cage-keeper/addresses/kovan-addresses.json',
        '--network', 'kovan',
        '--max-errors', '100',
        '--vat-deployment-block', '17707858',
        '--debug'
    ]
    CageKeeper(cage_args).main()
