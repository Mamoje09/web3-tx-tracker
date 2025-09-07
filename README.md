# Ethereum Transaction Tracker 🚀  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Web3.py](https://img.shields.io/badge/Web3.py-Blockchain-green)
![Etherscan API](https://img.shields.io/badge/Etherscan-API-orange)
![Excel](https://img.shields.io/badge/Export-CSV%2FExcel-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

A professional Python tool that fetches, displays and exports Ethereum transactions (ETH + ERC-20) for any wallet.  
Built with **Web3.py**, **Etherscan API** and lightweight CSV/Excel support (no pandas required).  

---

## ✨ Features
- ✅ Fetch **ETH transactions** from the Etherscan API  
- ✅ Fetch **ERC-20 token transactions** (e.g., USDC)  
- ✅ Pretty-printed results in clean tables (via `tabulate`)  
- ✅ Export results to **CSV** and **Excel (.xlsx)**  
- ✅ Works on **Python 3.13+** (future-proof, no pandas dependency)  
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

📸 Demo Output

ETH Transactions
=== Last ETH Transactions ===
╒══════════════╤══════════════╤══════════════╤═══════════════╤════════════════════╕
│ TX Hash      │ From         │ To           │ Amount (ETH)  │ Time (UTC)         │
╞══════════════╪══════════════╪══════════════╪═══════════════╪════════════════════╡
│ 0x8e4c3a...  │ 0xabc123...  │ 0xdef456...  │ 0.15000       │ 2025-09-05 20:15:44 │
╘══════════════╧══════════════╧══════════════╧═══════════════╧════════════════════╛

USDC Transactions
=== Last USDC Transactions ===
╒══════════════╤══════════════╤══════════════╤════════════════╤════════════════════╕
│ TX Hash      │ From         │ To           │ Amount (USDC)  │ Time (UTC)         │
╞══════════════╪══════════════╪══════════════╪════════════════╪════════════════════╡
│ 0x1f7c8b...  │ 0x123abc...  │ 0x456def...  │ 250.0000       │ 2025-09-05 18:45:20 │
╘══════════════╧══════════════╧══════════════╧════════════════╧════════════════════╛

Exported Files

✅ Exported 5 ETH transactions → eth_transactions.csv / eth_transactions.xlsx

✅ Exported 5 USDC transactions → usdc_transactions.csv / usdc_transactions.xlsx


🛠 Roadmap

Support multiple ERC-20 tokens (DAI, LINK, UNI, etc.)

Add ERC-721 (NFT) transaction tracking

Export directly to Google Sheets

Build a simple FastAPI dashboard for web display

📬 About Me

I’m Mamo (GitHub: mamoje09

I'm a backend engineer diving into Web3.

This is my second Web3 project, showcasing live blockchain data fetching, ERC-20 tracking and CSV/Excel exports — optimized for Python 3.13+.

---

## ⚙️ Setup

### 1. Clone the repo
```bash
git clone https://github.com/mamoje09/web3-tx-tracker.git
cd web3-tx-tracker
