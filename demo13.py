import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.authenticate({'username': 'admin', 'password': 'admin'})
    await page.goto('https://static3.scrape.cuiqingcai.com/')
    print(await page.content())
    await browser.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
