# 企業導入 GitHub Copilot 資安研究

## 1. 數據保護原則 (Data Protection)
GitHub Copilot for Business/Enterprise 承諾：
- **不使用企業代碼進行訓練**：企業客戶的 Snippets 不會被儲存或用於訓練公共模型。
- **加密傳輸**：所有數據皆透過 TLS 傳輸。

## 2. 合規性檢查點 (Compliance Checkpoints)
- **IP Protection**：啟用「Block suggestions matching public code」以避免版權爭議。
- **Vulnerability Scanning**：AI 產出的代碼必須通過公司內部的安全開發生命週期 (SDL) 檢查。

## 3. Visual Studio 設定建議
- 確保 Visual Studio 更新至 17.10+ 以獲得最佳的狀態管理。
- 透過 `Tools > Options` 集中管理 Copilot 狀態。
