📰 Web Scraper for News Headlines

🚀 Objective
This project is a simple web scraper that extracts top headlines from a news website and saves them into a `.txt` file for offline viewing or further analysis.

 🛠️ Tools & Technologies
- Python
- requests
- BeautifulSoup (bs4)


📁 Deliverables
- `scraper.py` – Python script to scrape headlines
- `headlines.txt` – Output file containing extracted news headlines

How It Works
1. The script sends a GET request to a specified news website using the `requests` library.
2. It uses `BeautifulSoup` to parse the HTML and locate headline elements like `<h2>` or `<h3>`.
3. The extracted headlines are saved line-by-line in `headlines.txt`.

📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/news-headline-scraper.git
   cd news-headline-scraper
