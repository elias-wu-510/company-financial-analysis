# company-financial-analysis — 改進追蹤

## 已改進

- [x] 新增 `references/improvement-priority-checklist.md`，把改進事項按 P0 / P1 / P2 分優先級。
- [x] 新增 `references/html-report-structure.md`，補足交付型 HTML 報告的結構要求。
- [x] 更新 `SKILL.md`，把 HTML 結構、MTR 案例、中文檢查清單、圖表質量檢查納入引用入口。
- [x] 強化 `assets/report_template.html`，從極簡模板升級為更像可交付報告的單文件 HTML 骨架。
- [x] 新增 `scripts/extract_pdf_text_with_pages.py`，補上頁碼級引用鏈前處理。
- [x] 新增 `scripts/build_source_period_map.py` 與 `references/source-period-map.md`，補上來源 / 年份 / 期別 mapping guardrail。
- [x] 新增 `scripts/check_metric_comparability.py`，補上混口徑與混期別檢查。
- [x] 新增 `scripts/normalize_units_and_labels.py`，補上單位 / 期別 / 標籤的 first-pass 標準化。

## 待改進

### P0
- [ ] 為 `extract_pdf_text.py` 增加頁碼 / 分段標記，方便引用鏈更穩。
- [ ] 補一個「來源-年份-期別 mapping」的小工具或模板，降低誤標年份風險。
- [ ] 補一個 chart comparability 自查模板，讓混口徑更不容易漏掉。

### P1
- [ ] 為更多公司 / 行業補 case notes（例如公用事業、電訊、地產平台）。
- [ ] 加入 peer comparison 的具體輸出骨架與最小比較維度。
- [ ] 增加技術指標白話化範例片段，讓非專業讀者更易讀。
- [x] 補 `normalize_units_and_labels.py`，統一單位 / 期別 / 標籤語言。
- [x] 補交付閉環與 v2→v3 驗收清單，讓報告可按 loop 反覆修訂後交付。

### P2
- [ ] 補更多 sector-specific metric keywords。
- [ ] 補常用 inline SVG 圖表模板。
- [ ] 視需要增加正式 `.skill` 打包與驗證流程輸出。
ific metric keywords。
- [ ] 補常用 inline SVG 圖表模板。
- [ ] 視需要增加正式 `.skill` 打包與驗證流程輸出。
