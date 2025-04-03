# 📈 Trading Bot for Bybit Based on Telegram Signals  

This program is designed for **automated trading on Bybit** using signals from private Telegram channels.  

## 🔧 Setup  

Before running the program, you need to enter your API keys provided by Bybit in the `listik.py` file. These keys allow the bot to place trades on your behalf.    

## 📑 Signal Analysis  

The program uses a `patterns` file that contains **predefined structures** for detecting key information in messages.  
- You can customize these patterns to match the format of signals from your preferred Telegram channels.  

## 🚀 How It Works  

1. **Run the program** and log in to Telegram.  
2. **Open the target Telegram channel** and scroll down to the latest message.  
3. The program **waits for new messages** and analyzes them based on the patterns defined in the `patterns` file.  
4. When a **new trading signal** arrives, the bot automatically **places an order on Bybit**.  

## ⚠ Important  

> **❗️ IMPORTANT:**  
> - The bot **does not process past messages**.  
> - It **waits for the next post** to execute a trade.  

---

💡 *Customize the `patterns` file to fine-tune how the bot detects trading signals!* 🚀  
