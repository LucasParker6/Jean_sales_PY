import { test, expect } from '@playwright/test';

test('test', async ({ page, browser }) => {

  //日期
  const date='20';
  const start_week='20';
  const end_week='26';

  //預期金額
  const expectedAmount = '1,200萬';
  const expectedAmount_02 = '1,200';
  const expectedAmount_03 = '0萬';

  //最大化視窗
  // const context = await browser.newContext({
  //   viewport: { width: 1920, height: 1080 } 
  // });

  //const newPage = await context.newPage();
  // await page.goto('https://devjeansalesadmin.webtech888.com/login');

  //縮放
  // await page.evaluate(() => {
  //   document.body.style.zoom = '0.8'; // 例如 1.2 表示 120% 的字體縮放
  // });

  //新增客戶
  await page.goto('https://devjeansalesadmin.webtech888.com/login');
  await page.getByPlaceholder('帳號').click();
  await page.getByPlaceholder('帳號').fill('Auto01');
  await page.getByPlaceholder('密碼').click();
  await page.getByPlaceholder('密碼').fill('123');
  await page.getByRole('button', { name: '登入' }).click();
  await page.getByRole('link', { name: '賞屋(客戶資料)管理' }).click();
  await page.getByRole('link', { name: '賞屋管理' }).click();
  await page.getByRole('button', { name: ' 新增' }).click();
  await page.getByPlaceholder('賞屋日期').click();
  await page.getByText(date, { exact: true }).click();
  await page.getByPlaceholder('客戶姓名').click();
  await page.getByPlaceholder('客戶姓名').fill('TEST02');
  await page.getByPlaceholder('手機號碼 ').click();
  await page.getByPlaceholder('手機號碼 ').fill('0911111111');
  await page.locator('#cdk-overlay-1 div').filter({ hasText: /^資料確認請選擇$/ }).getByRole('button').click();
  await page.locator('#nb-option-30').click();
  await page.locator('div').filter({ hasText: /^業務員\*請選擇$/ }).getByRole('button').click();
  await page.locator('xpath=/html[1]/body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[2]/div[3]/div[1]/nb-option-list[1]/ul[1]/nb-option[1]').click();
  await page.locator('div').filter({ hasText: /^第一次來訪是否購買 \*請選擇$/ }).getByRole('button').click();
  await page.getByText('已購', { exact: true }).click();
  await page.getByRole('button', { name: '確定' }).click();
  
  // 新增銷售前日報表
  await page.waitForTimeout(3000);
  await page.getByRole('link', { name: '報表管理' }).click();
  await page.getByRole('link', { name: '日報表' }).click();
  await page.getByRole('button', { name: ' 新增' }).click();
  await page.waitForTimeout(3000);
  await page.getByLabel('廣告媒體 *備註限制1000字').click();
  await page.getByLabel('廣告媒體 *備註限制1000字').fill('TEST');
  await page.locator('ngx-multiple-sales-selector').getByRole('button', { name: '請選擇' }).click();
  //await page.locator('xpath=/html[1]/body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[2]/div[4]/div[1]/nb-option-list[1]/ul[1]/nb-option[1]').click();
  await page.locator('nb-option').filter({ hasText: 'Auto01' }).click();
  await page.getByPlaceholder('主委').click();
  await page.getByPlaceholder('主委').fill('TSET');
  await page.getByPlaceholder('專案').click();
  await page.getByPlaceholder('專案').fill('TEST');
  await page.getByRole('button', { name: '確定' }).click();

  //比對日報表
  await page.locator('xpath=//tbody/tr[1]/td[7]/button[3]').click();

  //提取日報表金額
  await page.waitForTimeout(3000);
  const actualAmount_03 = (await page.locator('//body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-report1-detial[1]/div[1]/nb-card[1]/nb-card-body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]').textContent())?.trim() || '';

  if (actualAmount_03 === expectedAmount) {
    console.log('新增銷售前日報表金額比對正確');
  } else {
    console.error(`新增銷售前日報表金額比對失敗，預期：${expectedAmount_03}，實際：${actualAmount_03}`);
  }

  //銷控表
  await page.getByRole('link', { name: '銷控管理' }).click();
  await page.getByRole('link', { name: '銷控表' }).click();
  //購買第一戶
  await page.getByRole('row', { name: '1' }).getByRole('cell').nth(1).click();
  await page.locator('div').filter({ hasText: /^客資編號\*$/ }).getByRole('button').click();
  await page.getByPlaceholder('搜尋').fill('TEST02');
  await page.getByText('[10215]TEST02(0911111111)').click();
  await page.getByPlaceholder('成交價格').click();
  await page.getByPlaceholder('成交價格').fill('500');
  await page.locator('ngx-sales-selector').getByRole('button', { name: '請選擇' }).click();
  await page.locator('nb-option[class*="ng-star-inserted"]').click();
  //await page.locator('#cdk-overlay-1 label').filter({ hasText: '車位' }).getByRole('button').click();
  await page.locator('xpath=//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]').click();
  await page.locator('ngx-park-selector').getByRole('button', { name: '請選擇' }).click();
  await page.getByText('B1-1').click();
  await page.getByPlaceholder('車位價格').click();
  await page.getByPlaceholder('車位價格').fill('100');
  await page.getByPlaceholder('銷售時間').click();
  await page.getByText(date, { exact: true }).click();
  await page.getByRole('button', { name: '確定' }).click();
  //購買第二戶
  await page.getByRole('row', { name: '1' }).getByRole('cell').nth(2).click();
  await page.locator('div').filter({ hasText: /^客資編號\*$/ }).getByRole('button').click();
  await page.getByPlaceholder('搜尋').fill('TEST02');
  await page.getByText('[10215]TEST02(0911111111)').click();
  await page.getByPlaceholder('成交價格').click();
  await page.getByPlaceholder('成交價格').fill('500');
  await page.locator('ngx-sales-selector').getByRole('button', { name: '請選擇' }).click();
  await page.locator('nb-option[class*="ng-star-inserted"]').click();
  //await page.locator('#cdk-overlay-1 label').filter({ hasText: '車位' }).getByRole('button').click();
  await page.locator('xpath=//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[9]/label[1]/button[1]').click();
  await page.locator('ngx-park-selector').getByRole('button', { name: '請選擇' }).click();
  await page.getByText('B1-2').click();
  await page.getByPlaceholder('車位價格').click();
  await page.getByPlaceholder('車位價格').fill('100');
  await page.getByPlaceholder('銷售時間').click();
  await page.getByText(date, { exact: true }).click();
  await page.getByRole('button', { name: '確定' }).click();

  // 新增銷售後日報表
  await page.waitForTimeout(3000);
  await page.getByRole('link', { name: '報表管理' }).click();
  await page.getByRole('link', { name: '日報表' }).click();
  // await page.getByRole('button', { name: ' 新增' }).click();
  // await page.getByLabel('廣告媒體 *備註限制1000字').click();
  // await page.getByLabel('廣告媒體 *備註限制1000字').fill('TEST');
  // await page.locator('ngx-multiple-sales-selector').getByRole('button', { name: '請選擇' }).click();
  // //await page.locator('xpath=/html[1]/body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[2]/div[4]/div[1]/nb-option-list[1]/ul[1]/nb-option[1]').click();
  // await page.locator('nb-option').filter({ hasText: 'Auto01' }).click();
  // await page.getByPlaceholder('主委').click();
  // await page.getByPlaceholder('主委').fill('TSET');
  // await page.getByPlaceholder('專案').click();
  // await page.getByPlaceholder('專案').fill('TEST');
  // await page.getByRole('button', { name: '確定' }).click();

  //比對日報表
  await page.locator('xpath=/html[1]/body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-report1[1]/nb-card[1]/nb-card-body[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/button[3]').click();

  //提取日報表金額
  const actualAmount_01 = (await page.locator('//body[1]/ngx-app[1]/ngx-pages[1]/ngx-one-column-layout[1]/nb-layout[1]/div[1]/div[1]/div[1]/div[1]/div[1]/nb-layout-column[1]/ngx-report1-detial[1]/div[1]/nb-card[1]/nb-card-body[1]/div[1]/div[2]/table[1]/tbody[1]/tr[3]/td[4]').textContent())?.trim() || '';

  if (actualAmount_01 === expectedAmount) {
    console.log('新增銷售後日報表金額比對正確');
  } else {
    console.error(`新增銷售後日報表金額比對失敗，預期：${expectedAmount}，實際：${actualAmount_01}`);
  }
  await page.waitForTimeout(3000);

  // //新增週報表
  // await page.getByRole('link', { name: '報表管理' }).click();
  // await page.getByRole('link', { name: '週報表' }).click();
  // await page.getByRole('button', { name: ' 新增' }).click();
  // await page.getByPlaceholder('週期').click();
  // await page.getByPlaceholder('週期').fill('TEST');
  // await page.getByPlaceholder('日期(起)').click();
  // await page.getByText('20', { exact: true }).click();
  // await page.getByPlaceholder('日期(迄)').click();
  // await page.getByText('26').click();
  // await page.getByPlaceholder('主委').click();
  // await page.getByPlaceholder('主委').fill('TEST');
  // await page.getByPlaceholder('專案').click();
  // await page.getByPlaceholder('專案').fill('TEST');
  // await page.getByPlaceholder('廣告比例').click();
  // await page.getByPlaceholder('廣告比例').fill('1');
  // await page.getByPlaceholder('廣告預算總額').click();
  // await page.getByPlaceholder('廣告預算總額').fill('1');
  // await page.getByPlaceholder('實支廣告預算').click();
  // await page.getByPlaceholder('實支廣告預算').fill('1');
  // await page.getByPlaceholder('本週工作重點').click();
  // await page.getByPlaceholder('本週工作重點').fill('TEST');
  // await page.getByPlaceholder('下週預計工作計畫').click();
  // await page.getByPlaceholder('下週預計工作計畫').fill('TEST');
  // await page.getByRole('button', { name: '下一步' }).click();
  // await page.getByRole('button', { name: '確定' }).click();

  // //比對週報表
  // await page.locator('xpath=//tbody/tr[1]/td[11]/button[3]').click();
  // await page.getByRole('button', { name: ' 結算' }).waitFor({ state: 'visible' });
  // await page.getByRole('button', { name: ' 結算' }).click();

  // //提取周報表金額
  // const actualAmount_02 = (await page.locator('//nb-card-body/div[1]/div[1]/div[1]/table[1]/tr[1]/td[7]/span[1]').textContent())?.trim() || '';

  // if (actualAmount_02 === expectedAmount_02) {
  //   console.log('周報表金額比對正確');
  // } else {
  //   console.error(`周報表金額比對失敗，預期：${expectedAmount_02}，實際：${actualAmount_02}`);
  // }

  //退戶
  //await page.waitForTimeout(5000);
  await page.getByRole('link', { name: '銷控管理' }).click();
  await page.getByRole('link', { name: '銷控表' }).click();
  await page.locator('xpath=//tbody/tr[3]/td[2]').waitFor({ state: 'visible' });
  await page.locator('xpath=//tbody/tr[3]/td[2]').click();
  // let clicked_01 = false; // 初始化點擊狀態
  // while (!clicked_01) {
  //   try {
  //     await page.locator('xpath=//tbody/tr[3]/td[2]').click();
  //     clicked_01 = true;
  //   } catch (error) {
  //     console.log('點擊失敗，重試中...');
  //     await page.waitForTimeout(500);
  //   }
  // }
  
  await page.getByPlaceholder('退戶日期').waitFor();
  await page.getByPlaceholder('退戶日期').click();
  await page.getByText(date, { exact: true }).waitFor({ state: 'visible' })
  await page.getByText(date, { exact: true }).click();
  await page.getByRole('button', { name: '請選擇' }).click();
  await page.getByText('單價不認同').click();
  await page.getByRole('button', { name: '確定' }).click();

  // await page.getByRole('link', { name: '銷控管理' }).click();
  // await page.getByRole('link', { name: '銷控表' }).click();
  await page.locator('xpath=//tbody/tr[3]/td[3]').waitFor({ state: 'visible' });
  //await page.waitForTimeout(1000);
  await page.locator('xpath=//tbody/tr[3]/td[3]').click();
  // let clicked_02 = false; // 初始化點擊狀態
  // while (!clicked_02) {
  //   try {
  //     await page.locator('xpath=//tbody/tr[3]/td[3]').click();
  //     clicked_02 = true;
  //   } catch (error) {
  //     console.log('點擊失敗，重試中...');
  //     await page.waitForTimeout(500);
  //   }
  // }
  
  await page.getByPlaceholder('退戶日期').waitFor();
  await page.locator('xpath=//nb-card-body/div[1]/div[1]/div[1]/div[2]/div[15]/div[2]/input[1]').click();
  await page.getByText(date, { exact: true }).waitFor({ state: 'visible' })
  await page.getByText(date, { exact: true }).click();
  await page.getByRole('button', { name: '請選擇' }).click();
  await page.getByText('單價不認同').click();
  await page.getByRole('button', { name: '確定' }).click();
});
