const puppeteer = require('puppeteer');

async function run() {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://www.google.com');
    await page.screenshot({ path: 'screenshot.png' });

    await browser.close();
}

run();
