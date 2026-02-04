# Visual Studio 攔截代理 (PII Interceptor) 實作指南

為了符合保險業資安規範，我們必須確保開發者在 Visual Studio 中使用 GitHub Copilot 時，任何敏感個資 (PII) 都不會離開企業內網。

## 1. 核心原理
本方案採用 **Mitmproxy** 作為本地透明代理。透過自定義的 Python 腳本，攔截發往 GitHub Copilot API 的所有 POST 請求，並在封包送出前即時偵測並屏蔽 PII 資料。

## 2. 腳本功能說明 (`scripts/pii_interceptor.py`)
- **身分證字號偵測**：自動識別台灣身分證格式並替換為 `[ID_MASKED]`。
*   **保單與電話**：過濾 10-12 位數字的保單編號與手機號碼。
*   **敏感詞屏蔽**：針對「姓名」、「住址」等保險業常見敏感詞進行掩碼。
*   **JSON 遞迴處理**：深入處理 Copilot 的請求 JSON 結構，確保 `prompt` 欄位中的內容被徹底清洗。

## 3. 快速啟動步驟

### A. 安裝環境
```bash
pip install mitmproxy
```

### B. 啟動攔截代理
```bash
# 啟動 mitmdump 並加載我們的 PII 攔截腳本
mitmdump -s scripts/pii_interceptor.py --listen-port 8080
```

### C. 設定 Visual Studio 代理
1. 開啟 Visual Studio。
2. 進入 `工具 (Tools)` > `選項 (Options)`。
3. 搜尋 `代理 (Proxy)`，設定為 `127.0.0.1:8080`。
4. **關鍵步驟**：需將 Mitmproxy 的 CA 憑證 (`~/.mitmproxy/mitmproxy-ca-cert.p12`) 安裝至系統「受信任的根憑證授權單位」，否則 Visual Studio 會因 SSL 檢查失敗而無法連線。

## 4. 安全建議
- **Milk-Local 整合**：此腳本建議執行於 Ted 本地端的 Milk-Local 節點，作為第一道安全防線。
- **規則持續更新**：應根據公司最新的個資清冊，持續擴充 `sensitive_keywords` 列表。
