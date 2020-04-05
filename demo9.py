import asyncio
from pyppeteer import launch

width, height = 1200, 768

async def main():
    browser = await launch(headless=False,
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    context = await browser.createIncognitoBrowserContext()
    page = await context.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
