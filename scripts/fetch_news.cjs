const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

async function run() {
  const browser = await puppeteer.launch({ 
    headless: true,
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  const page = await browser.newPage();
  
  await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36');

  const sections = [
    { name: '정치', url: 'https://news.naver.com/section/100', count: 2 },
    { name: '경제', url: 'https://news.naver.com/section/101', count: 3 },
    { name: '세계', url: 'https://news.naver.com/section/104', count: 2 },
    { name: 'IT/과학', url: 'https://news.naver.com/section/105', count: 2 }
  ];

  let allNews = [];

  for (let sec of sections) {
    try {
      await page.goto(sec.url, { waitUntil: 'networkidle2', timeout: 30000 });
      const news = await page.evaluate((category, maxCount) => {
        const items = [];
        const nodes = document.querySelectorAll('.sa_item_inner');
        for (let i = 0; i < nodes.length; i++) {
          if (items.length >= maxCount) break;
          const node = nodes[i];
          const titleA = node.querySelector('.sa_text_title');
          const lede = node.querySelector('.sa_text_lede');
          const img = node.querySelector('.sa_thumb_link img');
          
          let imgSrc = null;
          if (img) {
              imgSrc = img.getAttribute('data-src') || img.src;
          }
          
          if (titleA && titleA.innerText.trim() !== '') {
            items.push({
              category: category,
              title: titleA.innerText.trim(),
              link: titleA.href,
              summary: lede ? lede.innerText.trim() : '',
              image: imgSrc
            });
          }
        }
        return items;
      }, sec.name, sec.count);
      allNews = allNews.concat(news);
    } catch (e) {
      console.error(`Failed to fetch news for ${sec.name}:`, e.message);
    }
  }

  // Fallback: Fetch OG images if missing
  for (let item of allNews) {
      if (!item.image) {
          try {
              await page.goto(item.link, { waitUntil: 'domcontentloaded', timeout: 10000 });
              const ogImage = await page.evaluate(() => {
                  const meta = document.querySelector('meta[property="og:image"]');
                  return meta ? meta.content : null;
              });
              if (ogImage) item.image = ogImage;
          } catch (e) {
              console.error('Failed to fetch OG image for', item.link);
          }
      }
  }

  await browser.close();

  const date = new Date();
  const dateString = date.getFullYear() + '년 ' + (date.getMonth() + 1) + '월 ' + date.getDate() + '일 ' + date.getHours() + ':' + String(date.getMinutes()).padStart(2, '0');
  
  let cardsHtml = '';
  for (let item of allNews) {
    cardsHtml += `
    <div class="card rounded-2xl overflow-hidden shadow-xl" onclick="window.open('${item.link}', '_blank')">
        ${item.image ? `<img src="${item.image}" class="w-full h-48 object-cover" alt="${item.title.replace(/"/g, '&quot;')}" loading="lazy">` : `<div class="w-full h-48 bg-slate-800 flex items-center justify-center text-slate-500">No Image</div>`}
        <div class="p-5">
            <span class="text-xs font-semibold text-sky-400 uppercase tracking-wider mb-2 block">${item.category}</span>
            <h2 class="text-xl font-bold mb-3 line-clamp-2 leading-tight">${item.title}</h2>
            <p class="text-slate-400 text-sm line-clamp-3 leading-relaxed">${item.summary}</p>
            <div class="mt-4 flex justify-end">
                <span class="text-sky-400 text-sm font-medium hover:underline">상세보기 →</span>
            </div>
        </div>
    </div>
    `;
  }

  const html = `<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="referrer" content="no-referrer">
    <title>Soul's 뉴스 자동사냥</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @import url('https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css');
        body { background-color: #0f172a; color: #f1f5f9; font-family: 'Pretendard', sans-serif; }
        .card { background-color: #1e293b; border: 1px solid #334155; transition: transform 0.2s ease; cursor: pointer; }
        .card:hover { transform: scale(1.02); }
        .gradient-text { background: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .nav-link { transition: color 0.2s; }
        .nav-link:hover { color: #38bdf8; }
    </style>
</head>
<body class="p-6">
    <div class="max-w-6xl mx-auto">
        <!-- 네비게이션 메뉴 바 -->
        <nav class="flex justify-between items-center mb-8 px-4 py-3 bg-slate-800/50 rounded-2xl border border-slate-700">
            <div class="font-bold text-lg gradient-text cursor-pointer" onclick="location.href='index.html'">Soul's 자동사냥포털</div>
            <div class="flex gap-6 text-sm font-medium text-slate-400">
                <a href="index.html" class="nav-link">
                    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="w-5 h-5"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>
                </a>
                <a href="news.html" class="text-sky-400">News</a>
                <a href="kospi.html" class="nav-link">KOSPI</a>
                <a href="nasdaq.html" class="nav-link">NASDAQ</a>
                <a href="valuation_semi.html" class="nav-link">Valuation</a>
            </div>
        </nav>

        <header class="mb-10 text-center">
            <h1 class="text-4xl font-extrabold mb-2 gradient-text">Soul's 뉴스 자동사냥</h1>
            <p class="text-slate-400 text-lg">주요 분야 최신 뉴스 실시간 자동사냥 | ${dateString}</p>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            ${cardsHtml}
        </div>

        <footer class="mt-12 text-center text-slate-500 text-sm">
            © 2026 Soul's 자동사냥포털. All analytical models are powered by Gemini Flash.
        </footer>
    </div>
</body>
</html>`;

  const outputPath = path.join(__dirname, '..', 'news.html');
  fs.writeFileSync(outputPath, html, 'utf8');
  
  console.log('HTML generated successfully at: ' + outputPath);
}

run().catch(console.error);