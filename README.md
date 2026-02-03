# GitHub Copilot 企業導入資安研究 (Visual Studio)

## 📌 研究目標
本專案針對企業在 Visual Studio 環境中導入 GitHub Copilot 的安全性、合規性及授權管理進行深入研究，並提供具體的資安檢查清單。

## 🛡️ 資安合規檢查清單 (Security & Compliance Checklist)

| 類別 | 檢查項目 | 說明 | 狀態 |
| :--- | :--- | :--- | :---: |
| **數據隱私** | 關閉「允許 GitHub 使用我的代碼進行模型改進」 | 確保企業專有代碼不會被用於訓練公共模型。 (GitHub Copilot for Business 預設關閉) | ☐ |
| **數據隱私** | 確認 Telemetry 傳輸範圍 | 檢查傳輸至 GitHub 的數據是否僅限於上下文片段，且符合企業加密傳輸標準。 | ☐ |
| **程式碼安全** | 啟用公共代碼過濾器 (Public Code Filter) | 防止 Copilot 建議與公共開源代碼完全相同的片段，避免潛在的版權與漏洞風險。 | ☐ |
| **程式碼安全** | 整合靜態分析工具 (SAST) | Copilot 生成的代碼仍需經過現有的資安掃描 (如 SonarQube) 檢查漏洞。 | ☐ |
| **存取管理** | 透過 GitHub Enterprise 控制權限 | 確保只有授權員工能使用 Enterprise 帳號登入 Visual Studio 並啟用服務。 | ☐ |
| **授權合規** | 檢查開源授權風險 | 監控 AI 生成代碼是否引入了 GPL 等傳染性授權協議的代碼片段。 | ☐ |
| **網路資安** | 配置企業代理伺服器 (Proxy) | 確保 Visual Studio 中的 Copilot 插件能透過受控的企業網路進行對外通訊。 | ☐ |

## 📚 參考資料
- [GitHub Copilot Trust Center](https://copilot.github.trust.page/)
- [Microsoft Learn: 管理 Visual Studio 中的 Copilot 狀態](https://learn.microsoft.com/zh-tw/visualstudio/ide/visual-studio-github-copilot-install-and-states?view=visualstudio)
- [Visual Studio 訂閱與定價](https://visualstudio.microsoft.com/zh-hant/vs/pricing/)

## 📄 詳細研究文件
- [網路配置與授權合規 (Proxy & Licensing)](./proxy_and_licensing.md)
- [數據保護原則 (Research Notes)](./research_notes.md)

