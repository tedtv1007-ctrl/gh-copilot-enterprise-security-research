# GitHub Copilot Business vs. Enterprise 比較研究與導入建議

## 1. 功能精簡比較摘要

| 功能項目 | Copilot Business (CB) | Copilot Enterprise (CE) |
| :--- | :--- | :--- |
| **主要定位** | 著重於 IDE 端的開發輔助 | 著重於全平台整合與企業知識庫轉化 |
| **IDE 輔助** | 包含 (Inline suggestions, Chat) | 包含 (與 CB 相同) |
| **GitHub.com 整合** | 無 | **包含 (Chat in GitHub.com, 總結 PR, 代碼解釋)** |
| **企業知識庫索引** | 無 | **可對指定 Repository 進行索引，提供脈絡化建議** |
| **客製化模型** | 無 | **支援私有微調模型 (Fine-tuned models) 預覽** |
| **CLI & Mobile** | 支援 | 支援 |
| **安全性控製** | 組織級政策、SAML SSO、IP 賠償 | 包含 CB 所有項目，更細緻的企業級控管 |

### 關鍵差異分析：
- **CB** 適合預算有限、且開發者主要僅在 IDE 內活動的團隊。
- **CE** 的核心價值在於「讓 Copilot 讀懂你的專案」，透過索引專案代碼，在 GitHub.com 上直接與代碼對話，極大化提升 Code Review 與 Onboarding 的效率。

---

## 2. 成本估算與授權分配建議 (Case: CB * 4 + CE * 1)

### 2.1 這種架構可行嗎？
**答案：技術上可行，但計費與權限分配需注意。**
在 GitHub Enterprise 帳戶下，你可以為不同的 Organization 分配不同的 Plan，或者在同一個 Enterprise 下混合指派 Seats。

### 2.2 費用試算 (以官方牌價為準)
- **Copilot Business:** $19 / user / month
- **Copilot Enterprise:** $39 / user / month

**情境 A：4個 CB + 1個 CE (分開指派)**
- 4 * $19 = $76
- 1 * $39 = $39
- **總計月費：$115**

**注意：** 如果同一個 User 被同時指派了 CB 和 CE 的 Seat，GitHub 會自動**只收一筆 CE 的錢 ($39)**，不會重複計費。

### 2.3 導入建議
初期購買 `4 Business + 1 Enterprise` 是非常聰明的 **PoC (概念驗證) 策略**：
- **1 個 CE Seat:** 分配給 **架構師或 Tech Lead**。他可以利用 CE 的功能來建立專案索引、設定自定義指令，並評估 GitHub.com 上的 Chat 功能對團隊 Code Review 的幫助。
- **4 個 CB Seats:** 分配給 **第一線開發者**。他們可以享受 IDE 內的加速，而不需要支付昂貴的 Knowledge Graph 授權。

---

## 3. 技術、安全與防火牆建議

### 3.1 安全性 (Security)
- **Data Exclusion:** 兩者皆預設不使用客戶代碼訓練模型。
- **Policy Management:** 建議管理員在 Enterprise 層級統一設定 `Public Code Filter` (建議開啟 `Blocked`)，防止輸出受版權保護的代碼片段。

### 3.2 防火牆與網路 (DLP/Network)
考慮到金融業的 DLP 環境，請確保以下 Domain 已加入白名單：
- `github.com` (基本操作)
- `api.github.com` (API 調用)
- `copilot-proxy.githubusercontent.com` (Copilot 通訊核心)
- `default.exp-actions.com` (遙測數據，可選)

---

## 4. 導入步驟 (Next Steps)
1. **驗證 Token 權限:** 確保目前的 PAT 具備 `enterprise:admin` 或 `manage_billing` 權限。
2. **小規模試點:** 照你提議的 4+1 模式，優先指派 1 名 Lead 測試 CE 的「專案索引」功能。
3. **效果評估:** 兩週後檢查 CE 是否顯著減少了 Lead 在解釋代碼脈絡上的時間。
