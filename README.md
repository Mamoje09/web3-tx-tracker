# Ethereum Transaction Tracker 🚀  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Web3.py](https://img.shields.io/badge/Web3.py-Blockchain-green)
![Etherscan API](https://img.shields.io/badge/Etherscan-API-orange)
![License](https://img.shields.io/badge/License-MIT-yellow)

A professional Python tool that fetches, displays and exports the last Ethereum transactions for any wallet.  
Built with **Web3.py**, **Etherscan API** and **Pandas** for CSV/Excel exports.  

---

## ✨ Features
- ✅ Fetch **ETH transactions** from the Etherscan API  
- ✅ Fetch **ERC-20 token transactions** (e.g., USDC)  
- ✅ Pretty-printed results in clean tables (using `tabulate`)  
- ✅ Export results to **CSV** and **Excel (.xlsx)**  
- ✅ Secure `.env` support for private keys and API tokens  


---

## 📂 Project Structure

web3_tx_tracker/

├── tx_tracker.py # Main script

├── requirements.txt # Dependencies

├── README.md # Documentation

├── .env # Local environment variables (ignored by Git)

└── screenshots/ # Demo outputs


---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/mamoje09/web3-tx-tracker.git
cd web3-tx-tracker
