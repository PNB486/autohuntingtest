import re

out = []
try:
    with open('news.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    articles = re.findall(r'<div class="card[^>]*>.*?<span class="text-xs font-semibold text-sky-400 uppercase tracking-wider">([^<]+)</span>.*?<span class="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-xs font-bold [^>]+>([^<]+)</span>.*?<h2 class="text-xl font-bold mb-3 line-clamp-2 leading-tight">([^<]+)</h2>', content, re.DOTALL)
    
    out.append(f"Found {len(articles)} articles.")
    for art in articles:
        category = art[0].strip()
        sentiment = art[1].strip()
        title = art[2].strip()
        out.append(f"[{category}] Sentiment: {sentiment} | Title: {title}")
except Exception as e:
    out.append(f"Error reading news.html: {e}")

with open("C:/Users/S/.gemini/antigravity-cli/brain/21a75728-0abd-4fe8-9f39-702e3af413a2/scratch/news_extracted.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))
print("News extraction complete.")
