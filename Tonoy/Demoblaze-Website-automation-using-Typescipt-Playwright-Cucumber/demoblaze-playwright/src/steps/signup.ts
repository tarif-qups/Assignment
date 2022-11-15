import { Given, When, Then } from "@cucumber/cucumber";
import { expect, _android } from "@playwright/test";
var {setDefaultTimeout} = require('@cucumber/cucumber'); setDefaultTimeout(60 * 1000);

// SignUp Rokomari Website

Given('User Open Rokomari Website', async function () {
    await global.page.goto('https://www.rokomari.com/book');
});
Then('Click Cross Button Of Add', async ()=> {
  await global.page.locator('(//i[@class="ion-close-round"])[2]').click()
})
Then('Click On Sign In Button', async()=> {
  await global.page.locator('//a[contains(text(), "Sign in")]').click();
})
Then('Click On Sign UP Button', async()=> {
  await global.page.locator('//p[contains(text(), "Sign up")]').click();
})
Then('Enter The Full Name', async()=> {
  await global.page.locator('#nm').fill('Abul')
})
Then('Enter The Email Name', async()=> {
  await global.page.locator("#js-email").fill('hasan.qups@gmail.com')
})
Then('Enter The Mobile Number', async()=> {
  await global.page.locator('(//input[@id="js-phone"])').fill('1798946719')
})
Then('Enter The Password Number', async()=> {
  await global.page.locator("#pwd").fill('12@#f3456')
})
Then('Select The Re-Captcha Check Box', async()=> {
  await global.page.locator('(//div[@role="presentation"]/..)[1]').click({force: true})
})
Then('Click On The Create Account Button', async ()=> {
  await global.page.locator('//button[contains(text(), "Create Account")]').click()
})
