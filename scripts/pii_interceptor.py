import re
import json
from mitmproxy import http

# --- 1. 定義保險業 PII 偵測邏輯 ---
class PIIDetector:
    def __init__(self):
        # 台灣身分證字號 Regex
        self.id_pattern = re.compile(r'[A-Z][12]\d{8}')
        # 台灣手機號碼 Regex
        self.phone_pattern = re.compile(r'09\d{8}')
        # 模擬保單號碼 Regex (假設為 10-12 位數字)
        self.policy_pattern = re.compile(r'\b\d{10,12}\b')
        # 敏感詞庫 (可持續擴充)
        self.sensitive_keywords = ['姓名', '住址', '地址', '出生日期', '受益人']

    def mask_text(self, text):
        if not text:
            return text
        
        # 替換身分證
        text = self.id_pattern.sub("[ID_MASKED]", text)
        # 替換手機
        text = self.phone_pattern.sub("[PHONE_MASKED]", text)
        # 替換保單號
        text = self.policy_pattern.sub("[POLICY_MASKED]", text)
        
        # 簡單的敏感詞替換 (可改用 NLP 實體識別模型強化)
        for kw in self.sensitive_keywords:
            text = text.replace(kw, "[SENSITIVE_KW]")
            
        return text

# --- 2. Mitmproxy 攔截插件 ---
class CopilotPIIInterceptor:
    def __init__(self):
        self.detector = PIIDetector()
        print("Milk-Local PII Interceptor 已啟動...")

    def request(self, flow: http.HTTPFlow) -> None:
        # 僅攔截 GitHub Copilot 的 API 端點
        # 常用端點: copilot-proxy.githubusercontent.com 或 api.githubcopilot.com
        if "githubcopilot.com" in flow.request.pretty_host or "githubusercontent.com" in flow.request.pretty_host:
            
            # 檢查是否為 JSON 格式的代碼建議請求
            if flow.request.method == "POST" and flow.request.content:
                try:
                    data = json.loads(flow.request.content)
                    
                    # 遞迴遍歷 JSON 並對所有字串值進行脫敏
                    processed_data = self._process_json(data)
                    
                    # 更新請求內容
                    flow.request.set_content(json.dumps(processed_data).encode("utf-8"))
                    print(f"[PII CLEANSED] 已過濾發往 {flow.request.pretty_host} 的敏感資訊")
                    
                except json.JSONDecodeError:
                    # 如果不是 JSON (可能是串流或其他格式)，改用純文字正則替換
                    content = flow.request.content.decode("utf-8", errors="ignore")
                    cleansed_content = self.detector.mask_text(content)
                    flow.request.set_content(cleansed_content.encode("utf-8"))

    def _process_json(self, obj):
        if isinstance(obj, dict):
            return {k: self._process_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._process_json(i) for i in obj]
        elif isinstance(obj, str):
            return self.detector.mask_text(obj)
        else:
            return obj

# 註冊插件
addons = [
    CopilotPIIInterceptor()
]
