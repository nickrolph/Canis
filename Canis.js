// const puppeteer = require('puppeteer-extra');
// const pluginStealth = require('puppeteer-extra-plugin-stealth');
// puppeteer.use(pluginStealth());

const puppeteer = require('puppeteer');

async function scrapeDogInfo(url){
    const browser = await puppeteer.launch();
    try {
        const page = await browser.newPage();
        await page.goto(url);

        const [el] = await page.$x('//*[@class="tweet-text"]');
        const src = await el.getProperty('src');
        const srcTxt = await src.jsonValue();

        console.log({srcTxt});
    } catch (e) {
        console.error(e.message);
    } finally {
        await browser.close();
    }

}

scrapeDogInfo('https://twitter.com/unicorndreams99/status/1272698084083085313');
