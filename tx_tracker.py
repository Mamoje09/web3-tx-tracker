import os
import requests
from dotenv import load_dotenv
from web3 import Web3
from datetime import datetime

load_dotenv()

provider = os.getenv("WEB3_PROVIDER")
etherscan_api_key = os.getenv("ETHERSCAN_API_KEY")
wallet = os.getenv("WALLET_ADDRESS")

if not provider or not wallet or not etherscan_api_key:
    raise SystemExit("❌ Please set WEB3_PROVIDER, WALLET_ADDRESS, and ETHERSCAN_API_KEY in .env")

w3 = Web3(Web3.HTTPProvider(provider))

def get_transactions(address, api_key, limit=5):
    url = (
        f"https://api.etherscan.io/api?module=account&action=txlist&address={address}"
        f"&startblock=0&endblock=99999999&sort=desc&apikey={api_key}"
    )
    response = requests.get(url, timeout=15).json()

    if response["status"] != "1":
        print("⚠️ No transactions found or API error.")
        return []

    return response["result"][:limit]

def print_tx_summary(tx_list):
    for tx in tx_list:
        ts = datetime.utcfromtimestamp(int(tx["timeStamp"])).strftime("%Y-%m-%d %H:%M:%S")
        value_eth = w3.from_wei(int(tx["value"]), "ether")
        print(f"\n🔹 TX Hash: {tx['hash']}")
        print(f"   From: {tx['from']}")
        print(f"   To: {tx['to']}")
        print(f"   Amount: {value_eth} ETH")
        print(f"   Time: {ts}")

if __name__ == "__main__":
    print(f"Fetching last 5 transactions for: {wallet}")
    txs = get_transactions(wallet, etherscan_api_key)
    print_tx_summary(txs)
