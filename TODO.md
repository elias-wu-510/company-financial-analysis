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
- [x] 新增 `references/delivery-loop.md`，把自查→改進→自查→改進→交付的閉環寫進 skill。
- [x] 新增 `references/internal-to-client-delivery.md`，把「先內部版，再客戶交付版」寫成正式工作流。
- [x] 新增 `references/v2-to-v3-acceptance-checklist.md`，把 reviewer feedback 驗收轉成可執行清單。
- [x] 新增 `references/external-retrieval-strategy.md`，把 Brave / 外部檢索納入官方來源優先的搜索流程。
- [x] 新增 `references/hkex-ir-retrieval.md`，把 Brave + 官方 IR + HKEX 文件檢索流程寫成可重複工作流。
- [x] 更新 `SKILL.md` workflow，明確做公司分析時把新聞 / 公告 / 外部動態當作默認應檢索的一層，再根據證據強度與期間匹配決定是否寫入報告。
- [x] 新增 `references/recent-news-window.md`，把最近三個月新聞 / 公告 / 更新的強制檢索寫成默認規則。
- [x] 新增 `references/news-driver-validation.md`，把新聞線補強與日期 / 期間映射驗證寫成工作流。
- [x] 新增 `references/latest-financial-statements-first.md`，把「最新官方財務報表優先、上一年報作基線」寫成默認分析原則。
- [x] 新增 `references/revenue-growth-and-upside.md`，把「收入增長與未來增長潛力是默認重點」寫成分析原則。
- [x] 新增 `references/report-style-light-theme.md`，把淺色、閱讀友好的報告風格寫成默認視覺規則。
- [x] 新增 `references/peer-comparison.md`，把同業比較變成可直接套用的分析骨架。
- [x] 新增 `references/peer-research-subagent-workflow.md`，把 peer research 交給 subagent、主 agent 專注主報告整合寫成正式工作流。
- [x] 新增 `references/plain-language-metrics.md`，補上面向普通讀者的核心指標白話模板。
- [x] 新增 `references/chart-templates.md`，把常用財務分析圖表骨架標準化。
- [x] 新增 `references/chart-final-sanity-check.md`，把客戶交付前的修圖 / 圖表最終審校寫成明確步驟。
- [x] 新增 `references/chart-sanity-scan.md` 與 `scripts/chart_sanity_scan.py`，把圖表數值-視覺一致性的半自動掃描能力補進 skill。
- [x] 更新 workflow，明確 client-delivery 版在發送前默認先跑一次 `chart_sanity_scan`。
- [x] 新增 `references/annual-report-openclaw-design-checklist.md`，把年報類交付的變化 / 趨勢 / 對比 / 未來定位要求寫成 checklist。
- [x] 新增公用事業 / 電訊 / 地產平台 case notes 三件套，補更多行業化分析框架。

## 待改進

### P0
- [x] 為 `extract_pdf_text.py` 增加頁碼 / 分段標記，方便引用鏈更穩。
- [x] 補一個「來源-年份-期別 mapping」的小工具或模板，降低誤標年份風險。
- [x] 補一個 chart comparability 自查模板，讓混口徑更不容易漏掉。

### P1
- [x] 為更多公司 / 行業補 case notes（例如公用事業、電訊、地產平台）。
- [x] 加入 peer comparison 的具體輸出骨架與最小比較維度。
- [x] 增加技術指標白話化範例片段，讓非專業讀者更易讀。
- [x] 補 `normalize_units_and_labels.py`，統一單位 / 期別 / 標籤語言。
- [x] 補交付閉環與 v2→v3 驗收清單，讓報告可按 loop 反覆修訂後交付。

### P2
- [ ] 補更多 sector-specific metric keywords。
- [x] 補常用 inline SVG / 圖表骨架模板。
- [ ] 視需要增加正式 `.skill` 打包與驗證流程輸出。
- [ ] 視使用情況補充更細的 Brave / 金融檢索 query pattern 範例。
- [ ] 視需要補一個 lightweight HKEX 文件抓取腳本雛形。
- [ ] 視需要把年報設計 checklist 再細化成數據層 / 敘事層 / 圖表層三份子清單。
- [ ] 視需要把 client-delivery 版再細化成簡報型 / 長報告型兩套模板。
- [ ] 視需要把新聞事件映射再做成可複用的資料層模板。
- [ ] 視需要把 chart sanity scan 擴展到 line / area / stacked charts。

## 下一階段：深度研究版升級路線

目標：把 `company-financial-analysis` 從「成熟 final draft / reviewer-sensitive 客戶稿」提升到可穩定支援 Level 2+ / Level 3 深度研究版公司分析。主 SKILL.md 保持精簡，深度能力優先放在 references/ 與必要 scripts/。

### Deep Research — P0（先補研究骨架）
- [ ] 新增 `references/multi-year-trend-analysis.md`
  - 定義 3 年 / 5 年趨勢拉取規則、優先指標、不能硬拉的情況、趨勢結論寫法。
- [ ] 新增 `references/peer-selection-framework.md`
  - 定義 peer 如何選、什麼叫可比 / 只能參考、peer comparison 的最小輸出骨架。
- [ ] 新增 `references/regional-and-segment-deep-dive.md`
  - 定義何時要做分區域 / 分業務深拆，如何把收入、利潤、戰略角色與風險接回整體 thesis。
- [ ] 更新 `SKILL.md` 入口規則
  - 當任務包含「深度研究 / 長期趨勢 / 同業比較 / 區域拆解 / 治理」等信號時，默認走 deep-research path，並讀取相應 references。

### Deep Research — P1（把深研版結構做穩）
- [ ] 新增 `references/deep-research-report-structure.md`
  - 固化深研版報告章節順序：summary / thesis / multi-year trend / segment-region / peers / balance sheet / governance / risks / conclusion。
- [ ] 新增 `references/capital-allocation-and-financing-history.md`
  - 補資本配置、融資歷史、hybrid / perpetual、再融資、CapEx 週期的分析框架。
- [ ] 新增 `references/governance-management-and-incentives.md`
  - 補治理、管理層、薪酬、激勵一致性何時值得寫、寫到什麼深度、如何避免寫成百科。

### Deep Research — P2（行業化深化與工具化）
- [ ] 新增 `references/deep-research-chart-templates.md`
  - 補多年趨勢、peer snapshot、capital structure evolution、region/segment panels 等圖表模板。
- [ ] 擴更多 deep-dive case notes
  - 例如 rail platform、utilities、telecom、property-linked platform 的深研版專項 notes。
- [ ] 視需要新增工具腳本
  - 例如 `scripts/build_multi_year_metric_panel.py`
  - 例如 `scripts/build_peer_snapshot_table.py`
  - 例如 `scripts/build_segment_region_matrix.py`
