# Marathi Social Media Post Generator

A web app that generates ready-to-post Marathi social media content for local businesses, built for a small electronics/furniture shop as the first use case. Give it a product or offer, and it returns a structured social media post — no manual translation or copywriting needed.

## Why this exists

Most AI content tools are built for English-first, generic marketing copy. Small Marathi-speaking businesses are underserved — they either skip social media entirely or rely on awkward direct translation. This tool generates content natively in Marathi, tuned for local business context.

## Features

- Generates structured social media post content in Marathi using the Gemini API
- Returns clean, structured JSON output (not raw unformatted text)
- Simple web interface to enter product/offer details and view the generated post
- Built to extend to other small businesses beyond the first use case

## Tech stack

- **Backend:** Python, Flask
- **AI:** Google Gemini API (`gemini-2.5-flash` via the `google-genai` library)
- **Frontend:** Jinja2 templates, HTML/CSS

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Create a virtual environment and activate it
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Gemini API key
   Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
   *(Check this matches the variable name your code actually reads — update if different.)*

5. Run the app
   ```bash
   python app.py
   ```
   Then open `http://localhost:5000` in your browser.

## Usage

Enter the product or offer details for the business, and the app returns a generated Marathi social media post you can copy and use directly.

## Roadmap

- [ ] Add support for multiple business types beyond electronics/furniture
- [ ] Add post history / saved drafts
- [ ] Deploy a live demo

## License

MIT — see [LICENSE](LICENSE).

## Author

Built by Namdev as part of a self-directed AI engineering learning path, focused on AI tools for local Marathi-speaking businesses.
