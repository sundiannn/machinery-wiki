# 操作紀錄

> 只能往後追加，不可修改舊紀錄（見 AGENTS.md 第 4.5 節）。

## [2026-11-22] schema | 建立 AGENTS.md 與專案骨架
- 討論：
  - 規則另開一份專用 AGENTS.md，不沿用課程筆記網站的規則
  - 與舊的課程筆記網站完全分開，所有內容從講義重新 ingest，不轉換舊筆記
  - wiki 只放在 GitHub（直接瀏覽 Markdown），不另做 wiki 網頁
  - 資料範圍：電機機械 Ch.1～Ch.5 講義，共 5 份；Ch.5 講義尚未放入 `raw/`
- 新增：AGENTS.md、README.md、wiki/index.md、wiki/log.md、slides/outline.md、slides/check.md
- 待確認：讀者設定、簡報頁數、lint 嚴格程度、簡報是否由另一個 AI 對話獨立檢查

## [2026-11-22] schema | 連結格式改為標準 Markdown
- 發現：初稿用 `[[檔名]]` 連結，但 wiki 是放在 GitHub 上給人瀏覽，GitHub 不會把 `[[...]]` 轉成可點的連結
- 修改：AGENTS.md 第 4.3 節改為一律使用相對連結 `[名稱](檔名.md)`；lint 第 1 項加入「誤用 `[[...]]`」的檢查

## [2026-11-23] schema | 依討論結果修改規則
- 討論：
  - 讀者：高中物理程度、沒修過電機；lint 維持現行規則
  - 例題：wiki 每章 1～2 題引導式例題頁（新增 `wiki/examples/`）；簡報全份最多 2 題
  - 簡報：維持**全部一份**、內分 5 章並有章節目錄，共 15～18 頁（使用者比較過「一章一份」後決定）
  - 簡報逐頁檢查交給另一個未參與製作的 AI，檢查者與生成者分離
  - 講義缺漏章節不自行補寫；手寫中文補充可採用並標註
- 修改：AGENTS.md 第 3、3.1、4.2.1（新增例題模板）、4.3、5.4、6.1、7.2 節

## [2026-11-23] ingest | Ch.1 電機機械原理導論
- 討論：
  - 使用者確認 11 個概念頁的切法（一個觀念一頁，`four-magnetic-principles` 當樞紐頁）
  - 例題改為「引導式解題頁」，Ch.1 選例 1-2（氣隙磁阻）、例 1-10（線性直流機）
  - 講義缺 1.9 節：不自行補寫，記為待確認
  - 左手定則與右手開掌定則並列，記入 AGENTS.md 7.2
- 新增：sources/ch01；concepts/electric-machines、rotational-motion、four-magnetic-principles、magnetic-field-and-permeability、magnetic-circuit、magnetization-curve、core-losses、faraday-law、induced-force、motional-voltage、linear-dc-machine；examples/ch01-air-gap、ch01-linear-machine
- 更新：index.md
- 數值核對：例 1-2（66,300／316,000／0.602 A）、例 1-6（100×0.05×377 = 1885 V）、例 1-10 各小題以計算重新驗證，皆與講義一致
- lint（新增 `tools/lint.py` 自動檢查第 1、2、3、4、8、9 項）：
  - 第 1 次：「缺少出處的條列」32 筆 → 檢查後發現多數是**誤判**：出處標在條列上方的小標，底下各點沒有重複標註
  - ✅ 修改 lint 腳本：小標或上層條列已標出處時，視為整組都有出處；第 2 次剩 3 筆巢狀條列誤判，再修正後 0 筆
  - ⏳ 待使用者確認：是否把「小標的出處涵蓋整組條列」寫進 AGENTS.md 4.3
  - 人工檢查（第 5～7 項）：無矛盾、無重複概念；發現符號 $\theta$ 在 Ch.1 同時代表「角位置」與「兩向量夾角」，各頁已在符號表分別說明 → 待使用者確認是否記入 7.2
- 待確認（TODO 4 筆）：1.9 節缺漏、p.28 左右手用字；兩筆「Ch.2～5 後補連結」屬預期中的待辦

## [2026-11-23] schema | 處理 Ch.1 遺留的待確認
- 討論：使用者表示「交給 AI 決定，全部完成後再回饋」。以下依 AI 先前提出的建議採用，之後各章的「討論」步驟改為 AI 列出決定並記錄在本 log，供使用者事後審閱
- 修改：AGENTS.md 4.3 加入「小標的出處涵蓋整組條列」；7.2 加入 $\theta$ 多義、$a$ 為匝數比

## [2026-11-23] ingest | Ch.2 變壓器
- 討論（AI 決定，使用者授權）：
  - 新增 11 個概念頁，`transformer` 當本章樞紐頁
  - 用 Ch.2 講義 p.5–6 建立 `ac-power`，補上 Ch.1 講義缺的 1.9 節（只寫 Ch.2 講義出現的內容）
  - 例題選例 2-1（輸電有無變壓器，適合初學者）與例 2-2（開路／短路測試，本章核心題型）
  - 2.11～2.13 節與例 2-4 不在講義內容中，不補寫
- 讀取方式：本章大部分公式與解答是圖片，文字擷取讀不到 → 改把 p.9–11、27–31、33–36、42–48、51–53 轉成圖像逐頁檢視
- 新增：sources/ch02；concepts/transformer、ac-power、ideal-transformer、real-transformer、transformer-equivalent-circuit、oc-sc-test、per-unit-system、voltage-regulation-and-efficiency、transformer-taps、autotransformer、three-phase-transformer；examples/ch02-transmission、ch02-oc-sc-test
- 更新：faraday-law、four-magnetic-principles、electric-machines、core-losses、magnetization-curve、magnetic-field-and-permeability（補上變壓器中的應用與連結）；sources/ch01（1.9 節待確認改為已處理）；index
- 數值核對：例 2-1（90.8 A、454 V、1484 W／95.94 A、9.594 A、479.7 V、16.7 W）、例 2-2（PF 0.234、144 Ω、34.63 Ω、38.4 + j192 Ω、159 kΩ、38.4 kΩ）皆與講義一致
- lint：
  - 第 1 次：缺出處 6 筆、缺符號表 1 筆
  - 檢查後：5 筆是「本章地圖」導覽清單被當成事實檢查、1 筆是兩個連續公式共用一張符號表 → ✅ 修改 lint：只檢查「正式內容」一節、連續公式共用符號表
  - 1 筆是真的放錯位置（electric-machines 的導覽連結寫在正式內容）→ ✅ 移到「和其他概念的關係」
  - 另發現 faraday-law 新增段落被插在「出處」前、位置錯誤 → ✅ 移回「正式內容」
  - 第 2 次：0 筆
  - 人工檢查：**發現矛盾**——例 2-1 講義註解「損失減少將近 90 %」與同頁數字（1484 W → 16.7 W，約 1/89）不符 → wiki 以數字為準並在例題頁說明，⏳ 待使用者確認
  - 人工檢查：$\phi$ 同時當「磁通」和下標「相」→ 記入 AGENTS.md 7.2

## [2026-11-23] ingest | Ch.3 交流電機基礎
- 討論（AI 決定，使用者授權）：
  - 新增 9 個概念頁，`ac-machines` 當本章樞紐頁；「電頻率與轉速」獨立一頁，因為簡報 Ch.3 會用到
  - **避免重複概念**：講義 3.7 的效率與 3.8 的電壓調整率，和 Ch.2 已有的 `voltage-regulation-and-efficiency` 是同一個定義 → 不另開頁，改為在既有頁加「發電機的電壓調整率」一節；只新增 `speed-regulation`
  - 例題只有例 3-2（講義沒有例 3-1），選它做引導頁
  - 3.6 節（繞組絕緣）只出現在目錄，不補寫
- 讀取方式：p.3、4、7、15、16、23–26、29、31–33 轉成圖像檢視公式
- 新增：sources/ch03；concepts/ac-machines、rotating-loop、rotating-magnetic-field、electrical-frequency-and-speed、air-gap-flux-distribution、ac-induced-voltage、ac-induced-torque、machine-losses-and-power-flow、speed-regulation；examples/ch03-simple-generator
- 更新：voltage-regulation-and-efficiency、electric-machines、four-magnetic-principles、induced-force、motional-voltage、core-losses、rotational-motion；index
- 數值核對：例 3-2（0.03 Wb、377 rad/s、169.7 V、120 V、208 V）與講義一致
- 自我修正：初稿 `ac-induced-voltage` 寫了一條沒有看圖確認的式子 → 回頭轉圖檢查 p.23，確認為 $e_{ind} = N_C\phi\omega\cos\omega t$（式 3-45）後改寫並補上推導條件
- lint：第 1 次「缺少出處」2 筆——功率流程圖的兩點寫在符號表之後，小標的出處不再涵蓋 → 屬**真問題**，✅ 補上出處；第 2 次 0 筆

## [2026-11-23] ingest | Ch.4 同步發電機
- 討論（AI 決定，使用者授權）：
  - 新增 6 個概念頁，`synchronous-generator` 當本章樞紐頁；電樞反應、同步電抗、相量圖合併在 `synchronous-equivalent-circuit`（三者是同一個模型的推導過程，拆開反而難讀）
  - 例題選例 4-1（測試求同步電抗，和例 2-2 想法相同，可跨章連結）與例 4-3（同樣 $E_A$ 下功因造成 410～535 V 的差異，最適合初學者）；兩題皆為講義標示的「考試重點」
  - 4.9～4.11 節只在目錄，不補寫
- 讀取方式：p.2、7、11、13、18–20、22、26–30 轉成圖像檢視
- 新增：sources/ch04；concepts/synchronous-generator、internal-generated-voltage、synchronous-equivalent-circuit、synchronous-power-and-torque、synchronous-machine-tests、generator-operating-alone；examples/ch04-parameter-test、ch04-power-factor
- 更新：ac-machines、four-magnetic-principles、magnetization-curve、oc-sc-test、ac-induced-torque、voltage-regulation-and-efficiency、electrical-frequency-and-speed；index
- 數值核對：例 4-1（0.2 Ω、311.8 V、1.02 Ω／1.04 Ω）、例 4-3（236.8／270.4／308.8 V → 410／468.4／535 V、34.1 kW、93.2%）以程式重算一致
- **發現講義手寫更正與矛盾**（圖像檢視才看得到，文字擷取看不到）：
  - p.2 式 (4-3) 的 $K$ 被老師劃掉改寫 → 採用手寫版，標〔講義手寫補充〕
  - 例 4-3 題目 50 Hz 被改成 60 Hz，但印刷解答仍用 50 Hz（1000 r/min）→ 兩者並列，⏳ 待使用者確認
- 工具修正：更新多個舊頁面的腳本在第 4 個檔案斷言失敗時，前 3 個已寫入、後面全部沒執行 → 改寫成共用的 `wikiedit` 函式並重跑，再以 lint 確認 index 與連結完整
- lint：第 1 次 index 缺 9 頁（上述腳本中斷造成）→ ✅ 修正；第 2 次 0 筆

## [2026-11-23] ingest | Ch.5 同步電動機
- 討論（AI 決定，使用者授權）：
  - 新增 5 個概念頁，`synchronous-motor` 當本章樞紐頁，並收錄 5.4 節「發電機與電動機的差別、P/Q 四種組合」（這是整門課的收尾觀念，放在樞紐頁最容易被簡報引用）
  - 例題選例 5-3（調場電流就讓輸電損失少 28%，不需要相量圖也看得懂，且可呼應例 2-1）
  - 5.5 節只在目錄，不補寫
- 讀取方式：p.2、7、20、21 轉成圖像檢視
- 新增：sources/ch05；concepts/synchronous-motor、synchronous-motor-torque-speed、v-curve、power-factor-correction、synchronous-motor-starting；examples/ch05-power-factor-correction
- 更新：synchronous-generator、ac-machines、four-magnetic-principles（清掉最後兩筆「之後補連結」TODO）、speed-regulation、ac-power（補 $Q = P\tan\theta$）、synchronous-power-and-torque、rotating-magnetic-field、electric-machines；index（Ch.1 的「電機」分類改名為「第一台電機（Ch.1）」，避免和其他章混淆）
- 數值核對：例 5-3（80.2／150／93 kVAR、PF 0.812／0.957、667／566 A、損失少 28%）以程式重算一致
- lint：0 筆需修正；剩 3 筆待使用者確認的 TODO

## [2026-11-23] lint | 全 wiki 跨章檢查（Ch.1～Ch.5）
- 機械檢查（tools/lint.py）：
  - 新增第 10 項「概念頁缺少模板區塊」→ 發現 6 頁沒有「白話解釋」（air-gap-flux-distribution、internal-generated-voltage、speed-regulation、synchronous-machine-tests、three-phase-transformer、transformer-taps）→ ✅ 補上
  - 結果：56 頁，0 筆需修正
- 人工檢查：
  - 符號跨章不一致 3 處 → 記入 AGENTS.md 7.2：$\delta$ 在 Ch.3 與 Ch.4 的兩種寫法其實等價；$K$ 與 $k$ 是不同常數；$\mathbf{I}_A$ 在發電機與電動機的參考方向相反
  - $\mathbf{I}_A$ 方向相反在 Ch.4 頁面沒有提醒，讀者可能混淆 → ✅ 在 synchronous-equivalent-circuit 加註並連到電動機頁
  - 重複概念：效率與電壓調整率在 Ch.2、Ch.3、Ch.4 都出現，已集中在 voltage-regulation-and-efficiency，其他頁只連結不重寫 → 無需合併
  - 跨章主題「同一台機器可當電動機也可當發電機」（Ch.1 線性直流機 ↔ Ch.5 同步電動機）原本沒有互連 → ✅ 補上連結（簡報故事線會用到）
- 仍待使用者確認（3 筆）：Ch.1 p.28 左右手用字、例 2-1「90 %」、例 4-3 頻率 50/60 Hz

## [2026-11-23] outline | 產生教學簡報大綱
- Query：只讀 wiki（index 與各章樞紐頁、概念頁、例題頁），產生 18 頁大綱（slides/outline.md），每頁標註依據的 wiki 頁
- 決定（AI，使用者授權）：例題引導選例 1-2（Ch.1）與例 5-3（Ch.5），頭尾各一題；其他例題（2-1、4-3、1-10）只放結論數字
- 與 AGENTS.md 6.1 的差異：Ch.1 第 4 頁原定「法拉第定律」，改為「線性直流機」，法拉第定律併入四大原理頁與理想變壓器頁 → 理由：線性直流機是「同一台機器可當發電機也可當電動機」的伏筆，Ch.5 要回扣

## [2026-11-23] slides | 生成 slides/index.html
- 依大綱生成單一 HTML（18 頁、章節目錄可跳轉、上方章節列、每頁 📖 連到 GitHub 上的 wiki 頁、鍵盤／按鈕／滑動換頁、KaTeX）
- 自我檢視（截圖逐頁看，不是正式檢查）：
  - SVG 圖中的 `$...$` 數學式不會被 KaTeX 處理 → 改成純文字
  - 第 18 頁（自我檢測）內容超出版面 → 改成三欄
  - 右下角換頁按鈕蓋住頁碼、第 8 頁圖說被裁切、第 14 頁長條圖頂端數字被裁切、第 4、6、10 頁圖中文字與圖形重疊 → 已修正

## [2026-11-23] schema | 依執行經驗修改規則（把檢查往前移）
- 修改：AGENTS.md
  - 5.1 Ingest「讀」步驟加入：公式、數字、例題解答一律看頁面圖像確認，未確認不得寫入 → 來源：Ch.2～Ch.4 公式多為圖片、Ch.3 曾寫入未確認的式子、Ch.4 的手寫更正只有圖像看得到
  - 5.3 Lint 加入第 10 項「概念頁模板區塊」，並註明可用 `tools/lint.py` 自動檢查 → 來源：跨章 lint 才發現 6 頁缺「白話解釋」，應在每次 ingest 就抓到
  - 第 3 節資料夾結構加入 `tools/`

## [2026-11-23] check | 簡報第 1 輪獨立檢查
- 檢查者：另一個 AI（子代理），只拿到 wiki 與簡報（不含講義、log、大綱）
- 結果：通過 9 頁、重生 9 頁（3、5、8、9、11、13、14、15、16），詳見 slides/check.md
  - **事實錯誤 1 頁**：第 3 頁把 wiki 的「磁通再大，只要不變…」改寫成「磁場再強…」，意思改變，還和同頁原理④矛盾
  - **誤導 1 頁**：第 14 頁把「每相」內生電壓 277 V 和「線間」端電壓 410～535 V 放在一起比，讀者會以為端電壓比內生電壓還高
  - **新手看不懂 8 頁**：定子／轉子、場電流、阻抗、電抗、相角、額定、激磁電流、功因、虛功率、感應電動機、轉矩角等名詞，在簡報中從未解釋就直接使用
- 判斷問題出在哪一層：
  - 第 3、14 頁：出在**生成簡報**（改寫 wiki 時走樣、數字挑選不當）→ 只重生該頁
  - 名詞問題：**一半出在 wiki**——講義預設讀者修過電路學，wiki 照講義整理，所以很多名詞在 wiki 裡也沒有白話定義（阻抗、電抗、相角、額定）→ 依規則**先回去修 wiki**

## [2026-11-23] ingest | 補 wiki：初學者名詞小抄（因簡報檢查而回頭修 wiki）
- 新增：concepts/beginner-glossary（講義有定義的照講義並標頁碼；阻抗的比喻、電抗不發熱、相角、額定等講義沒定義的，標〔AI 補充〕）
- 更新：electric-machines（連到小抄）、index
- lint：0 筆

## [2026-11-23] slides | 依第 1 輪檢查重生 9 頁（v2）
- 只重生 3、5、8、9、11、13、14、15、16 頁，其餘 9 頁不動
- 第 3 頁：改回「穿過線圈的磁通變化」並說明和原理④的差別；data-src 補上 induced-force、motional-voltage
- 第 5 頁：補「串聯相加」步驟、說明 $\mu_0$、轉子／定子加括號
- 第 8、9、16 頁：在首次出現處白話解釋一次繞組、阻抗、相角、電抗、激磁電流、額定、實功率／虛功率、功因、感應電動機；data-src 加入 beginner-glossary
- 第 11、13、15 頁：定義定子／轉子、場電流（並補上「場電流→磁通→電壓」因果鏈）、轉矩角；第 15 頁表格改成「轉子磁場在前／在後」，不用相量說法
- 第 14 頁：方程式改成白話；長條圖加上「無載 480 V」參考線，不再和每相 277 V 比；解釋功因、落後、超前
- 同時採納 5 項次要建議（第 7、10、17、18 頁用字與出處）
- 自我檢視：第 5 頁內容被頁尾蓋住、第 14 頁圖中標籤重疊 → 已修正

## [2026-11-23] schema | 把「新手看得懂」的檢查往前移到大綱階段
- 原因：第 1 輪簡報檢查 9 頁不通過，其中 8 頁是名詞沒解釋；這種問題在**寫大綱時**就看得出來，不該等到簡報做完才由檢查者抓到
- 修改：AGENTS.md 5.4 步驟 A，大綱每頁必填「本頁首次出現的術語」，且術語的白話解釋必須先存在於 wiki；slides/outline.md 補上此欄（v2）

## [2026-11-23] check | 簡報第 2 輪獨立檢查
- 檢查者：另一個新的子代理（沒看過第 1 輪報告）
- 結果：通過 16 頁、重生 2 頁（14、15），詳見 slides/check.md
  - 第 14 頁：白話公式「端電壓＝內生電壓－壓降」照字面讀會以為端電壓一定變小，但同頁長條圖超前時 535 V > 480 V，**v2 修正時引入的新矛盾**；「單位功因」比定義早出現；「電感」沒解釋
  - 第 15 頁：**事實錯誤**——把轉矩角寫成「轉子與定子旋轉磁場之間」的角度，wiki 定義是 $\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ 的夾角；「淨磁場」「轉矩」沒定義
  - 判斷：兩頁問題都出在**生成簡報**（白話化時把意思簡化錯了），wiki 本身正確 → 只重生該頁

## [2026-11-23] slides | 依第 2 輪檢查重生第 14、15 頁（v3）
- 第 14 頁：說明「扣」是考慮步調的扣法，結果可能變小也可能變大；在本頁定義功因數字、單位功因；「電感」改成「線圈本身的電抗（第 9 頁）」
- 第 15 頁：照 wiki 定義淨磁場與轉矩角；「轉矩」加括號（扭力，引用 rotational-motion）；data-src 補 synchronous-equivalent-circuit、rotational-motion、beginner-glossary
- 同時採納 8 項次要建議（第 3、4、5、6、9、10、11、13、16 頁補符號說明、統一「相角」用詞、補資料來源）

## [2026-11-23] check | 簡報第 3 輪獨立檢查
- 檢查者：另一個新的子代理（沒看過前兩輪報告）
- 結果：**18 頁全部通過**，0 頁重生
- 第 3 輪後採納 3 項次要建議（第 3 頁補「N 是匝數」、第 9 頁「只」改「幾乎只」以符合 wiki 原文、第 16 頁補「由功因算出電流」），皆為直接引用 wiki 的用字微調，未再送檢；截圖確認版面無溢出

## [2026-11-23] schema | 完成
- README.md 填寫繳交項目 1～6（執行結果與反思）
- 最終狀態：wiki 56 頁（來源 5、概念 43、例題 8），lint 0 筆需修正；簡報 18 頁，第 3 輪獨立檢查全部通過
- 待使用者確認：3 筆講義問題（見 README 第 5 節）；所有概念頁仍為 `status: draft`，等使用者審閱後改為 `checked`

## [2026-11-23] schema | 使用者要求改版
- 使用者要求：
  1. GitHub Pages 網頁只顯示簡報、不顯示 wiki，網頁名稱改為「電機機械教學簡報」
  2. README 不放作業繳交內容（繳交整理由使用者自己做）
  3. 簡報畫面不標示出處；文字太多的頁面精簡成重點
  4. 增加概念動畫與換頁動畫
- 發現：上傳時 `.nojekyll` 沒有傳上 GitHub（Windows 隱藏了以「.」開頭的檔案），所以 Pages 用 Jekyll 把 README 顯示成首頁 → 把簡報移到 repo 根目錄 `index.html`，首頁就是簡報
- 修改：AGENTS.md 第 3 節（簡報位置）、5.4 步驟 B、6.2（不顯示出處，改以隱藏 `data-src` 與 outline.md 追溯；動畫內容也須有 wiki 依據；每頁只講重點）；README 改為專案說明；`slides/index.html` 改為轉址到首頁；outline.md 註記 v4

## [2026-11-23] slides | 簡報 v4：首頁化、精簡文字、加入動畫與互動
- 18 頁主題與依據不變；每頁內文改成短句；新增換頁轉場、元素依序浮現，以及 8 頁概念動畫／互動（見 slides/outline.md）
- 自我檢視：截圖逐頁確認無溢出、無 console 錯誤

## [2026-11-23] check | 簡報第 4 輪獨立檢查（本輪起動畫內容也列入檢查）
- 結果：通過 13 頁、重生 5 頁（4、8、13、14、16），詳見 slides/check.md
  - **動畫事實錯誤**：第 8 頁圖畫 6 匝對 2 匝（3 : 1），波形振幅卻是 60 : 24（2.5 : 1），和同頁公式 $V_P/V_S = N_P/N_S$ 矛盾——文字檢查抓不到，只有讀動畫程式碼才發現
  - 精簡文字時造成的問題：第 4 頁括號「長度 ÷ 導磁係數 × 面積」運算順序錯；第 4、13 頁刪掉了術語說明（導磁係數、$E_A$）；第 14 頁功因沒說數值方向；第 16 頁刪掉兩台感應電動機的功率與功因，讀者算不出步驟 1
- 修正：重生 5 頁（振幅改 60 : 20），並採納 5 項次要建議（第 3 頁受力動畫方向、第 6 頁用字、第 9 頁短路測試說明、第 11 頁合成磁場長度更接近 1.5 倍、第 14 頁落後／超前的說法）

## [2026-11-23] check | 簡報第 5 輪獨立檢查
- 結果：**18 頁全部通過**，詳見 slides/check.md
- 之後採納 3 項用字微調（第 3、4、16 頁），未再送檢；截圖確認無溢出、無錯誤
