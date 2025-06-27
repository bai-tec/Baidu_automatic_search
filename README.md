# 百度关键词自动搜索与代理检测工具

## 项目简介

本项目包含两个实用工具：

1. **百度关键词自动搜索工具（main.py）**  
   - 支持批量关键词自动在百度搜索，支持代理池、随机PC端User-Agent，自动点击搜索结果，适合SEO测试、曝光提升等场景。
   - 支持便携式分发，无需用户安装Python或Playwright环境。

2. **代理HTTPS检测工具（ip_test.py）**  
   - 批量检测代理IP是否支持百度的HTTPS访问，输出响应速度和可用性。

---

## 目录结构
├── main.py # 百度关键词自动搜索主程序 
├── ip_test.py # 代理HTTPS检测工具 
├── keywords.txt # 关键词列表，每行一个关键词 
├── proxies.txt # 代理池列表，每行一个代理（ip:端口），可为空 
├── ms-playwright/ # Playwright浏览器内核文件夹，便携分发用


---

## 使用方法

### 1. 关键词自动搜索

- **准备文件**  
  - `keywords.txt`：每行一个关键词
  - `proxies.txt`：每行一个代理（格式如 `ip:端口`），可为空
  - `ms-playwright` 文件夹：与 exe 或 main.py 同目录

- **运行方式**  
  - Python环境下：`python main.py`
  - 打包后：双击 exe 文件

- **主要功能**  
  - 自动循环所有关键词，依次进行百度搜索
  - 支持代理池，失败自动切换代理重试，确保每个关键词都能成功搜索
  - 随机PC端User-Agent，模拟真实用户
  - 支持便携式分发，无需用户安装Playwright

### 2. 代理HTTPS检测

- **准备文件**  
  - `proxies.txt`：每行一个代理（ip:端口）

- **运行方式**  
  - Python环境下：`python ip_test.py`

- **主要功能**  
  - 检测所有代理是否支持百度HTTPS访问，输出响应速度和可用性

---

## 注意事项

- 关键词和代理文件请用 UTF-8 编码保存。
- `ms-playwright` 文件夹需与主程序同目录，便于无依赖分发。
- 如需观察浏览器操作过程，可将 `headless=True` 改为 `headless=False`。
- 本工具仅供学习和测试使用，请勿用于非法用途。

---

## 常见问题

- **程序一闪而过/无输出？**  
  检查 `keywords.txt` 是否有内容，且与主程序在同一目录。

- **提示找不到浏览器内核？**  
  确保 `ms-playwright` 文件夹完整且与主程序同目录。

- **代理失败太多？**  
  检查 `proxies.txt` 代理是否可用、支持 HTTPS。

---

## License

MIT

---

**欢迎 star 和反馈建议
