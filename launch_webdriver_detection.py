import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})

    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')

    await page.evaluate(
        '''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
