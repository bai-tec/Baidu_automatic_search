from playwright.sync_api import sync_playwright
import random
import time
import os
import sys

if getattr(sys, 'frozen', False):
    base_dir = os.path.dirname(sys.executable)
else:
    base_dir = os.path.dirname(os.path.abspath(__file__))
os.environ["PLAYWRIGHT_BROWSERS_PATH"] = os.path.join(base_dir, "ms-playwright")


# 自定义User-Agent池，随时可扩展
uas = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"
]


def load_list(filename):
    with open(filename, encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def main():
    keywords = load_list('keywords.txt')
    proxies = load_list('proxies.txt')
    batch_num = 1

    while True:
        print('━━' * 50)
        print(f"搜索启动：第{batch_num}批次")
        batch_start = time.time()

        with sync_playwright() as p:
            for keyword in keywords:
                if proxies:
                    tried_proxies = set()
                    while True:
                        if len(tried_proxies) == len(proxies):
                            tried_proxies.clear()
                        proxy = random.choice(proxies)
                        if proxy in tried_proxies:
                            continue
                        tried_proxies.add(proxy)
                        user_agent = random.choice(uas)

                        browser_args = {}
                        browser_args['proxy'] = {"server": f"http://{proxy}"}
                        try:
                            browser = p.chromium.launch(headless=True, **browser_args)
                            context = browser.new_context(user_agent=user_agent)
                            page = context.new_page()

                            page.goto("https://www.baidu.com", timeout=20000)
                            page.fill('input[name=\"wd\"]', keyword)
                            page.keyboard.press('Enter')
                            page.wait_for_selector('#content_left', timeout=10000)
                            links = page.query_selector_all('#content_left a')
                            if links:
                                link = random.choice(links)
                                link.click()
                                time.sleep(random.uniform(2, 5))
                            else:
                                time.sleep(random.uniform(2, 4))
                            print(f"搜索：{keyword} 代理成功:{proxy}")
                            break
                        except Exception:
                            print(f"搜索：{keyword} 代理失败：{proxy}")
                        finally:
                            try:
                                page.close()
                                context.close()
                                browser.close()
                            except:
                                pass
                else:
                    user_agent = random.choice(uas)
                    print(f"搜索：{keyword} 代理为None，采用本机IP搜索")
                    try:
                        browser = p.chromium.launch(headless=True)
                        context = browser.new_context(user_agent=user_agent)
                        page = context.new_page()

                        page.goto("https://www.baidu.com", timeout=20000)
                        page.fill('input[name=\"wd\"]', keyword)
                        page.keyboard.press('Enter')
                        page.wait_for_selector('#content_left', timeout=10000)
                        links = page.query_selector_all('#content_left a')
                        if links:
                            link = random.choice(links)
                            link.click()
                            time.sleep(random.uniform(2, 5))
                        else:
                            time.sleep(random.uniform(2, 4))
                        print(f"搜索：{keyword} 本机IP成功")
                    except Exception:
                        print(f"搜索：{keyword} 本机IP失败")
                    finally:
                        try:
                            page.close()
                            context.close()
                            browser.close()
                        except:
                            pass
                time.sleep(random.uniform(1, 5))

        batch_end = time.time()
        minutes = (batch_end - batch_start) / 60
        print(f"搜索完毕：第{batch_num}批次  用时：{minutes:.2f}分钟")
        print('━━' * 50)

        batch_num += 1


if __name__ == "__main__":
    main()
