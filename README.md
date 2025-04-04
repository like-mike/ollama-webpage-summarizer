# 🧠 Website Summarizer (Terminal Edition)

This is a quick and dirty script that uses [Ollama](https://ollama.com) and a local LLM (LLaMA 3.2 in this case) to fetch a website, strip out navigation noise, and give you a concise summary in markdown — all from your terminal.

## 🛠️ How It Works

- You pass in a URL.
- It grabs the site's title and text content.
- Sends it to the LLM with a system prompt to summarize it in markdown.
- Prints the result to your terminal.

## 🧩 Dependencies

- [Ollama](https://ollama.com) running locally with a model like `llama3.2`
- Python packages listed in `requirements.txt`

Install them with:

```bash
pip install -r requirements.txt
