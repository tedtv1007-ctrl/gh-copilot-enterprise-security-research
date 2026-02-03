# 企業管理員策略設定指南 (Enterprise Policy Management)

在企業導入 GitHub Copilot 時，組織管理員 (Organization Owners) 可透過 GitHub 後台強制執行多項資安與合規策略，確保開發過程符合公司規範。

## 1. 策略設定路徑
1. 登入 GitHub，進入組織的首頁。
2. 點擊 **Settings** (設定)。
3. 在左側選單的 "Code, planning, and automation" 區塊下，點擊 **Copilot**。
4. 選擇 **Policies** (策略) 標籤。

---

## 2. 關鍵資安策略設定

### A. 建議代碼與公共代碼比對 (Suggestions matching public code)
*   **功能**：偵測 Copilot 的建議是否與 GitHub 上的公共代碼有超過 150 個字元的重複。
*   **建議設定**：**Block** (阻斷)。
*   **資安價值**：避免引入具有 Copyleft 授權 (如 GPL) 的代碼片段，降低智慧財產權風險。

### B. Copilot 在 GitHub.com 的使用 (Copilot in GitHub.com)
*   **功能**：控制使用者是否能在 GitHub 網頁版（如 Pull Requests, Issues）中使用 AI 輔助功能。
*   **建議設定**：根據內部開發流程決定。若需強化代碼審查，建議開啟。

### C. Copilot Chat 功能管理 (Copilot Chat in IDEs)
*   **功能**：決定使用者是否能在 Visual Studio 等 IDE 中使用聊天功能。
*   **建議設定**：**Enabled**。Chat 功能可協助解釋現有安全漏洞並提供修正建議。

### D. 模型選擇策略 (Models)
*   **功能**：管理可供使用的 AI 模型（如 GPT-4o, Claude 3.5 Sonnet 等）。
*   **建議設定**：限制僅能使用企業審核過的模型，避免數據處理不透明。

---

## 3. 隱私與反饋設定

*   **User Feedback Collection** (用戶反饋收集)：建議 **關閉**。避免員工在反饋中無意間包含敏感的代碼片段或業務邏輯。
*   **Preview Features** (預覽功能)：建議 **關閉**。預覽功能的數據處理方式可能尚未通過企業的正式資安評估。

---

## 4. 席位管理與授權撤銷
*   **Seat Management**：管理員應定期稽核授權名單，針對離職員工或專案變動即時撤銷 (De-provision) 授權。
*   **Usage Logs**：透過 GitHub Audit Logs 監控 Copilot 的啟用狀態與異常活動。

---

## 5. 總結：企業最佳實踐
1. **強制執行全域策略**：若組織隸屬於 Enterprise，應由 Enterprise 層級統一下達策略，防止個別組織自行放寬標準。
2. **定期合規檢查**：每季度檢查一次 Copilot 策略設定，確保與最新的法規要求保持一致。
