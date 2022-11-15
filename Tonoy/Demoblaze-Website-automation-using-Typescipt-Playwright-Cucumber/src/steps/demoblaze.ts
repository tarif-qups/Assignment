import { Given, When, Then } from "@cucumber/cucumber";
import { expect, _android } from "@playwright/test";
const elements = require('../Locators/locators')
const data = require('../TestData/data')
var {setDefaultTimeout} = require('@cucumber/cucumber'); setDefaultTimeout(60 * 1000);

// <------------------------------------------------------------------->
// <----------------------- Signup Steps ------------------------------->
// <------------------------------------------------------------------->

Given('User Open demoblaze Website', async function () {
    await global.page.goto('https://demoblaze.com/');
});

When('Click signup', async ()=> {
  await global.page.locator(elements.signup).click()
})
Then('type sign up user name', async()=> {
  await global.page.locator(elements.signup_username).fill(data.USERNAME)
})

Then('type sign up user password', async()=> {
  await global.page.locator(elements.signup_password).fill(data.PASSWORD)
})

Then('Click close button', async()=> {
  await global.page.locator(elements.signup_close).click()
})

                              // Assertation
Then('Check element present or not', async()=> {
  await expect (global.page.locator(elements.signup_assertation)).toHaveCount(1)

  if (await global.page.$(elements.signup_assertation)){
    await global.page.locator(elements.signup_assertation).click()
  }
})

Then('check element hidden or visisble', async()=> {
  await expect(global.page.locator(elements.signup_assertation)).toBeVisible()
  // await expect(global.page.locator(elements.signup_assertation)).toBeHidden()
})

Then('check text', async()=> {
  await expect(global.page.locator(elements.signup_assertation)).toHaveText("PRODUCT STORE")
  // await expect(global.page.locator(elements.signup_assertation)).not.toHaveText("PRODUCT STORE")
})

Then('check attribute', async()=> {
  // await expect(global.page.locator(elements.signup_assertation)).toHaveAttribute('class', 'navbar-brand')
  await expect(global.page.locator(elements.signup_assertation)).toHaveClass('navbar-brand')
})

Then('check page url and title', async()=> {
  await expect(global.page).toHaveURL('https://demoblaze.com/index.html')
  await expect(global.page).toHaveTitle('STORE')
})

// <------------------------------------------------------------------->
// <----------------------- Login Steps ------------------------------->
// <------------------------------------------------------------------->

When('Click login', async ()=> {
  await global.page.locator(elements.login).click()
})
Then('type login user name', async()=> {
  await global.page.locator(elements.login_username).fill(data.USERNAME)
})

Then('type login user password', async()=> {
  await global.page.locator(elements.login_password).fill(data.PASSWORD)
})

Then('Click login close button', async()=> {
  await global.page.locator(elements.loginp_close).click()
})

Then('check login page title', async()=> {
  await expect(global.page).toHaveURL('https://demoblaze.com/')
  await expect(global.page).toHaveTitle('STORE')
})



// <------------------------------------------------------------------->
// <----------------------- Cart Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on cart', async ()=> {
  await global.page.locator(elements.cart).click()
})

Then('click on place order', async ()=> {
  await global.page.locator(elements.place_order).click()
})

Then('type place order name', async()=> {
  await global.page.locator(elements.place_order_name).fill(data.Name)
})

Then('type place order country', async()=> {
  await global.page.locator(elements.place_order_country).fill(data.Country)
})

Then('type place order city', async()=> {
  await global.page.locator(elements.place_order_city).fill(data.City)
})

Then('type place order credit card', async()=> {
  await global.page.locator(elements.place_order_credit_card).fill(data.Credit_card)
})

Then('type place order month', async()=> {
  await global.page.locator(elements.place_order_month).fill(data.Month)
})

Then('type place order year', async()=> {
  await global.page.locator(elements.place_order_year).fill(data.Year)
})

Then('click on place order close', async()=> {
  await global.page.locator(elements.place_order_close).click()
})

Then('check cart page title', async()=> {
  await expect(global.page).toHaveURL('https://demoblaze.com/cart.html')
  await expect(global.page).toHaveTitle('STORE')
})


// <------------------------------------------------------------------->
// <----------------------- About Us Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on about us', async ()=> {
  await global.page.locator(elements.about_us).click()
})

// Then('click on video', async ()=> {
//   await global.page.locator("//div[@class='vjs-poster']").click()
// })

// Then('click on pause video', async ()=> {
//   await global.page.locator("//video[@id='example-video_html5_api']").click()
// })

Then('click on about us close', async ()=> {
  await global.page.locator(elements.about_us_close).click()
})

// <------------------------------------------------------------------->
// <----------------------- Contact Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on contact', async ()=> {
  await global.page.locator(elements.contact).click()
})

Then('type contact email name', async()=> {
  await global.page.locator(elements.contact_email).fill(data.contact_email)
})

Then('type contact name', async()=> {
  await global.page.locator(elements.contact_Name).fill(data.contact_name)
})

Then('type contact message', async()=> {
  await global.page.locator(elements.contact_message).fill(data.message)
})

Then('click on contact', async ()=> {
  await global.page.locator(elements.contact_close).click()
})

// <------------------------------------------------------------------->
// <----------------------- Home phones Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on Home', async ()=> {
  await global.page.locator(elements.home).click()
})

Then('click on home phone', async ()=> {
  await global.page.locator(elements.home_phone).click()
})

Then('click on phone nexus6', async ()=> {
  await global.page.locator(elements.phone_nexus6).click()
})

Then('click on add to cart', async ()=> {
  await global.page.locator(elements.add_to_cart).click()
})

Then('click on home cart', async ()=> {
  await global.page.locator(elements.home_cart).click()
})

Then('click on cart delete', async ()=> {
  // await global.page.waitForSelector(elements.cart_delete, {state: "visible"});
  // await global.page.waitForSelector(".foo .bar", {state: "hidden"})
  await global.page.locator(elements.cart_delete).click()
})

// <------------------------------------------------------------------->
// <----------------------- Home laptops Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on laptops', async ()=> {
  await global.page.locator(elements.home_laptops).click()
})

Then('click on laptops sony', async ()=> {
  await global.page.locator(elements.laptops_sony).click()
})

Then('click on add to laptops add to cart', async ()=> {
  await global.page.locator(elements.laptops_add_to_cart).click()
})

Then('click on laptops cart', async ()=> {
  await global.page.locator(elements.laptops_cart).click()
})

Then('click on laptops cart delete', async ()=> {
  await global.page.waitForSelector(elements.laptops_cart_delete, {state: "visible"});
  await global.page.locator(elements.laptops_cart_delete).click()
})

// <------------------------------------------------------------------->
// <----------------------- Home monitors Steps ------------------------------->
// <------------------------------------------------------------------->

When('click on monitors', async ()=> {
  await global.page.locator(elements.home_monitors).click()
})

Then('click on monitors apple', async ()=> {
  await global.page.locator(elements.monitors_apple).click()
})

Then('click on add to monitors add to cart', async ()=> {
  await global.page.locator(elements.monitors_add_to_cart).click()
})

Then('click on monitors cart', async ()=> {
  await global.page.locator(elements.monitors_cart).click()
})

Then('click on monitors cart delete', async ()=> {
  await global.page.waitForSelector(elements.monitors_cart_delete, {state: "visible"});
  await global.page.locator(elements.monitors_cart_delete).click()
})