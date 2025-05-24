import csv
import time
import re
import json
import logging
from datetime import datetime
import unicodedata
import requests

OUTPUT_CSV = "cushion_skintific_akun_1.csv"
CHECKPOINT_FILE = "checkpoint.json"
LOG_FILE = "scraper.log"
API_BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"  
KEYWORDS = ["cushion skintific", "skintific cushion"]
MAX_BATCHES = 10
TWEETS_PER_BATCH = 10
SLEEP_INTERVAL = 15 * 60  
LANG = "id"

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

def clean_text(text):
    text = unicodedata.normalize("NFKD", text)
    text = re.sub(r"http\S+", "", text)  
    text = re.sub(r"@\w+", "", text)     
    text = re.sub(r"#\w+", "", text)     
    text = re.sub(r"[^\w\s]", "", text)  
    return text.strip()

def save_checkpoint(batch):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"last_batch": batch}, f)

def load_checkpoint():
    try:
        with open(CHECKPOINT_FILE, "r") as f:
            return json.load(f).get("last_batch", 0)
    except FileNotFoundError:
        return 0

def save_to_csv(data):
    fieldnames = ["author_name", "text", "clean_text", "created_at"]
    try:
        with open(OUTPUT_CSV, "x", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    except FileExistsError:
        pass

    with open(OUTPUT_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)

def load_existing_data():
    existing = set()
    try:
        with open(OUTPUT_CSV, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row["author_name"], row["text"])
                existing.add(key)
    except FileNotFoundError:
        pass
    return existing

def fetch_tweets(keyword):
    url = f"https://api.twitter.com/2/tweets/search/recent"
    headers = {"Authorization": f"Bearer {API_BEARER_TOKEN}"}
    params = {
        "query": f"{keyword} lang:{LANG}",
        "max_results": TWEETS_PER_BATCH,
        "tweet.fields": "created_at",
        "expansions": "author_id",
        "user.fields": "name",
    }
    response = requests.get(url, headers=headers, params=params, timeout=15)
    response.raise_for_status()
    return response.json()

def scrape():
    existing = load_existing_data()
    start_batch = load_checkpoint()

    for batch in range(start_batch, MAX_BATCHES):
        logging.info(f"🟡 Memulai batch ke-{batch + 1}")
        all_new_data = []

        for keyword in KEYWORDS:
            try:
                data = fetch_tweets(keyword)
                tweets = data.get("data", [])
                users = {user["id"]: user["name"] for user in data.get("includes", {}).get("users", [])}

                for tweet in tweets:
                    author_name = users.get(tweet["author_id"], "Unknown")
                    text = tweet["text"]
                    key = (author_name, text)

                    if key in existing:
                        continue

                    clean = clean_text(text)
                    new_entry = {
                        "author_name": author_name,
                        "text": text,
                        "clean_text": clean,
                        "created_at": tweet["created_at"],
                    }
                    all_new_data.append(new_entry)
                    existing.add(key)

                logging.info(f"✅ Keyword '{keyword}' berhasil ambil {len(tweets)} tweet")

            except Exception as e:
                logging.error(f"❌ Gagal ambil tweet keyword '{keyword}': {e}")
                continue

        if all_new_data:
            save_to_csv(all_new_data)
            logging.info(f"📦 Tersimpan {len(all_new_data)} tweet baru ke CSV")
        else:
            logging.info("⚠️ Tidak ada data baru untuk disimpan")

        save_checkpoint(batch + 1)
        logging.info(f"⏸️ Tidur selama {SLEEP_INTERVAL / 60} menit...")
        time.sleep(SLEEP_INTERVAL)

    logging.info("🎉 Selesai scraping semua batch")

scrape()