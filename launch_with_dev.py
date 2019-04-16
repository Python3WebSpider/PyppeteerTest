import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
