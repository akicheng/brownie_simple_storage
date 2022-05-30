from lib2to3.pgen2.literals import simple_escapes
from brownie import accounts,  config, SimpleStorage
import os
from dotenv import load_dotenv
load_dotenv()

def test_deploy():
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
    account = accounts.add(config["wallets"]["from_key"]);
    print(account)
    write_value=0
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    assert stored_value == write_value

def test_update():
    write_value=15 
    account = accounts.add(config["wallets"]["from_key"]);
    simple_storage = SimpleStorage.deploy({"from": account})
    simple_storage.store(write_value,{"from": account})
    assert simple_storage.retrieve()    == write_value