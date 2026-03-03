from patchright.async_api import async_playwright
import asyncio

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        # Kiro GitHub login URL
        url = "https://prod.us-east-1.auth.desktop.kiro.dev/login?idp=Github&redirect_uri=http%3A%2F%2F127.0.0.1%3A19823%2Fkiro-social-callback&code_challenge=8kKJdGppfo6T55srjGrlvwY9z6_tt_bkDC3YyQnQjLU&code_challenge_method=S256&state=u4QHLar2mpbGqESHUa9J7h69z0WXF9ZDfBAh2MuPFac"
        
        await page.goto(url)
        print(await page.title())
        print(await page.content())
        
        await browser.close()

asyncio.run(main())
