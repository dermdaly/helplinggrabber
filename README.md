# Helpling Invoice Downloader

A Python script that automates logging into the Helpling customer portal and downloading all your invoices — even if the list is virtualized and only partially loaded as you scroll.

## ✅ Features

- Scrolls through Helpling’s virtualized invoice list.
- Detects and clicks each invoice to trigger a download.
- Avoids duplicates by tracking already processed items.
- Saves all PDFs to a local `downloads/` folder.

## 🚀 Setup

1. **Clone the repository:**

    git clone https://your.repo.url
    cd helpling-invoice-downloader

2. **Create and activate a virtual environment:**

    python3 -m venv venv
    source venv/bin/activate

3. **Install required packages:**

    pip install -r requirements.txt

> 💡 Note: Don’t commit the `venv/` directory — add it to `.gitignore`.

## 🧪 Usage

Run the script like this:

    python download_invoices.py

1. Chrome will launch and navigate to the Helpling login page.
2. Log in **manually**.
3. Once logged in, return to the terminal and press Enter to begin the download process.
4. The script will scroll the list, click each invoice, and trigger downloads.

## 📁 Output

All downloaded invoices will be saved in:

    ./downloads/

You can change the target folder in the script if needed.

## 🧹 Updating Requirements

If you add new packages during development:

    pip freeze > requirements.txt

## 🛠 Troubleshooting

- **Only 10 invoices downloading?**  
  That’s normal on first attempt — Helpling uses a *virtualized list*. This script now scrolls incrementally and processes invoices in batches.

- **Script doesn’t quit?**  
  There’s a failsafe to stop after a few scrolls with no new items, but you can adjust `max_scroll_attempts` in the script.

## 📄 License

MIT License (or any license you prefer).