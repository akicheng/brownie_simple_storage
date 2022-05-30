from eth_typing import ContractName
from brownie import accounts, config, SimpleStorage

def read_contract():
    for i in range(len(SimpleStorage)):
        print(SimpleStorage[i])

def main():
    read_contract()