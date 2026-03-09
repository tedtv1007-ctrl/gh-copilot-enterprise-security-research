# 【內部簽呈/申請草案】GitHub Copilot 企業開發輔助工具導入計畫

## 一、 計畫背景與目的
為提升軟體開發效率並強化代碼品質，擬導入 GitHub Copilot AI 開發輔助工具。本計畫旨在透過 AI 自動化補全、代碼解釋及專案知識庫索引功能，降低開發人員在撰寫重複性代碼及理解遺留系統（Legacy Code）上的負擔。

## 二、 導入方案建議：混合授權模式 (Hybrid Seat Allocation)
考量成本效益與功能完整性，建議採購 **5 個授權座位 (Seats)**，並依職責分配如下：

| 授權等級 | 數量 | 單價 (月) | 分配對象 | 核心功能應用 |
| :--- | :--- | :--- | :--- | :--- |
| **Copilot Enterprise (CE)** | 1 | $39 | **技術架構師 / Lead** | **專案索引 (Knowledge Graph)**、GitHub.com Chat、PR 總結、安全性與架構諮詢。 |
| **Copilot Business (CB)** | 4 | $19 | **核心開發人員** | IDE 內代碼自動補全 (Autocomplete)、代碼重構建議、快速錯誤偵測。 |
| **預估總月費** | **5** | **$115** | | (相較全數購買 Enterprise 節省 41% 費用) |

## 三、 技術安全性與合規說明 (針對金融/產險業環境)
1. **代碼隱私 (Privacy):** 根據 GitHub 官方條款，Business/Enterprise 等級**絕不**使用客戶的私人代碼 or Prompt 進行模型訓練，確保機敏資訊不外洩。
2. **版權保護 (IP Indemnity):** 包含智慧財產權補償保障，並建議管理員開啟「Block suggestions matching public code」過濾器，降低侵權風險。
3. **網路合規 (DLP/Firewall):** 需於公司防火牆開放 `copilot-proxy.githubusercontent.com` 及 `api.github.com` 等特定 Domain，以確保 AI 模型正常連線。

## 四、 預期效益 (PoC 階段)
1. **開發加速：** 預計降低 25%-40% 的重複代碼撰寫時間。
2. **加速專案理解：** 透過 Enterprise 專案索引功能，新進人員或 Lead 可在 GitHub.com 直接詢問代碼架構，縮短 50% 的 Onboarding 與 Code Review 時間。
3. **優化代碼質量：** AI 即時檢測潛在 Bug 與安全性漏洞，提升初版代碼的穩定度。

## 五、 下一步行動
1. **正式採購申請：** 提交採購流程購買 5 Seats。
2. **環境部署：** 由 IT/資安部門協助調整防火牆白名單。
3. **PoC 評估：** 試行兩個月後，視 CE 專案索引功能的使用頻率與成效，再決定是否擴大 CE 授權比例。
