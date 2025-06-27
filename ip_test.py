import requests
import msvcrt
import time


def test_https_proxy(proxy):
    proxies = {
        "http": f"http://{proxy}",
        "https": f"http://{proxy}",
    }
    try:
        start = time.time()
        resp = requests.get("https://www.baidu.com", proxies=proxies, timeout=5)
        elapsed = time.time() - start
        if resp.status_code == 200:
            print(f"{proxy} 支持HTTPS，响应时间：{elapsed:.2f} 秒")
        else:
            print(f"{proxy} 不支持HTTPS，状态码：{resp.status_code}")
    except Exception as e:
        print(f"{proxy} 不支持HTTPS，原因：{e}")


with open("proxies.txt", encoding="utf-8") as f:
    proxy_list = [line.strip() for line in f if line.strip()]
print('        ====================== 工具-检测IP对百度的HTTPS的支持 ======================\n')
print(f"共检测{len(proxy_list)}个代理")
print('━━'*50)
for proxy in proxy_list:
    test_https_proxy(proxy)
print('━━'*50)
print("\n测试完成，按 ESC 键退出程序...")
while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\x1b':  # ESC
            break