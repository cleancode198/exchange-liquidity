from brownie import SushiswapExchangeRemove, accounts

def main():
    acct = accounts.load("deployer_account")
    # SushiswapExchangeAdd.deploy({"from":acct, "gasPrice":100 * 10 ** 9})
    SushiswapExchangeRemove.deploy({"from":acct})