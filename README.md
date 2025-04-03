### 📈 Trading Bot for Bybit Based on Telegram Signals
This program is designed for automated trading on Bybit using signals from private Telegram channels.
### 🔧 Setup
Before running the program, the user must enter API keys provided by Bybit. These keys are required to execute trades directly on the exchange.
### 📑 Signal Analysis
The program uses a patterns file that contains predefined structures for detecting key information in messages. Users can customize these patterns to adapt the bot to their specific signal formats.
### 🚀 How It Works
Launch the program and log in to Telegram.
Open the target channel and scroll down to the latest message.
The program waits for new messages and analyzes them based on the patterns configurations.
When a new trading signal arrives, the program automatically places an order on Bybit.
##### ⚠ Important: The bot does not process past messages. It waits for the next post to execute a trade.
