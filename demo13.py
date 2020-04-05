import asyncio
from typing import Dict

from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://static3.scrape.cuiqingcai.com/')
    await page.authenticate(Dict['admin', 'admin'])
    print(await page.content())
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
