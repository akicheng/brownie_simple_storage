from brownie import accounts,  config, SimpleStorage, network
import os
from dotenv import load_dotenv
load_dotenv()

def deploy_simple_storage():
    ####brownie-default gnache account###
    #account = accounts[0];
    #print(account)
    ####brownie-Command Line insert###
    #account = accounts.load("freecodecamp-account");
    #print(account)
    ####brownie-config.yaml-method1###
    #account = accounts.add(os.getenv("PRIVIATE_KEY"));
    #print(account)
    ####brownie-config.yaml-method2 with wallet###
    #network.connect("rinkeby")
    #account = accounts.add(config["wallets"]["from_key"]);
    #print(account)
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print("Initial stored value=",stored_value)
    write_value=15 
    transaction = simple_storage.store(write_value,{"from": account})
    transaction.wait(1)
    print("write New value ",write_value,"....")
    stored_value = simple_storage.retrieve()
    print("stored value=",stored_value)
    ##account2 = accounts.add(config["wallets"]["from_key2"]);
    ##print(account2)

def get_account():
    if(network.show_active()=='development'):
        return accounts[0] #Ganache CLI
    else:
        return accounts.add(config["wallets"]["from_key"]);
    print(account)

def main():
    print("Hello World!")
    deploy_simple_storage()
