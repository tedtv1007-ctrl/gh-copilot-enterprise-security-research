# 企業訂閱與定價指南 (Subscription & Pricing)

針對企業導入 GitHub Copilot，除了 GitHub 端的授權外，Visual Studio 的訂閱層級也會影響整體開發工具鏈的資安與管理能力。

## 1. Visual Studio 訂閱層級對比

| 項目 | Professional (每月/標準) | Enterprise (每月/標準) | 說明 |
| :--- | :--- | :--- | :--- |
| **定價 (估計)** | ~$45 USD / 月 | ~$250 USD / 月 | 標準版通常包含更多 Azure 點數與長期軟體下載權限。 |
| **GitHub Enterprise** | 選購項 | **包含於標準版中** | Enterprise 標準版通常直接包含 GitHub Enterprise 授權。 |
| **資安功能** | 基本 SAST | **進階代碼掃描與分析** | Enterprise 版本提供更深入的靜態分析與架構設計工具。 |
| **Azure DevOps** | 基本功能 | **包含 Test Plans** | 對於需要嚴格測試合規的企業，Test Plans 是關鍵。 |
| **支援事件** | 2 個 | **4 個** | Enterprise 提供更高等級的技術支援優先權。 |

---

## 2. GitHub Copilot 授權方案

| 方案 | Copilot Business | Copilot Enterprise |
| :--- | :--- | :--- |
| **價格 (每席位)** | $19 USD / 月 | $39 USD / 月 |
| **數據隱私** | 不使用代碼訓練模型 | 不使用代碼訓練模型 |
| **SSO / SAML** | 支援 | 支援 |
| **自定義模型** | ❌ 僅限基礎模型 | ✅ **支援針對企業代碼庫進行索引 (Indexing)** |
| **PR 摘要生成** | ❌ 不支援 | ✅ **支援** |
| **知識庫整合** | ❌ 不支援 | ✅ **可連結 Wiki.js 或企業內部文檔** |

---

## 3. 採購決策建議 (Decision Matrix)

### A. 小型開發團隊 / 初創企業
- **建議組合**：Visual Studio Professional + GitHub Copilot Business。
- **理由**：成本最低，同時保有基本的代碼隱私保護與 SSO 整合。

### B. 中大型企業 / 產險業 (資安高度要求)
- **建議組合**：**Visual Studio Enterprise (標準版) + GitHub Copilot Enterprise**。
- **理由**：
    1.  **整合授權**：VS Enterprise 標準版直接包含 GitHub Enterprise，簡化採購流程。
    2.  **知識庫優勢**：Copilot Enterprise 可索引企業內部的「核保手冊」與「理賠規範」，對業務流程有顯著加速作用。
    3.  **進階合規**：提供更細緻的稽核日誌 (Audit Logs) 與權限控管。

---

## 4. 隱藏成本與注意事項
*   **Azure 點數抵扣**：VS Enterprise 標準版每月提供 $150 USD 的 Azure 點數，可用於部署測試環境中的 Keycloak 或 Wiki.js。
*   **席位浪費**：建議搭配 GitHub API 自動檢查超過 30 天未活躍的 Copilot 席位並自動回收，以節省成本。
