import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')
    # 后退
    await page.type('#q', 'iPad')
    # 关闭
    await asyncio.sleep(10)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
