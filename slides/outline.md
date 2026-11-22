# 教學簡報大綱

> 由 Query 步驟產生，只根據 wiki（見 AGENTS.md 第 5.4 節步驟 A）。
> 使用者已授權 AI 決定（2026-11-23），確認後生成 `index.html`。

- 狀態：已產生（2026-11-23）；v2 依第 1 輪檢查新增「本頁首次出現的術語」欄，並把簡報第 3、5、8、9、11、13～16 頁的依據更新為重生後的版本（加入 beginner-glossary 等）
- 讀者：具備高中物理程度、沒修過電機的人
- 故事線：「電怎麼變成動、動怎麼變成電？」——從磁場的四個原理出發，經過變壓器、旋轉磁場，最後發現發電機和電動機是同一台機器
- 例題引導：2 題（例 1-2、例 5-3），其餘例題只放結論並連到 wiki

| 頁 | 段落 | 標題 | 學習目標（讀者看完能說出…） | 要點 | 依據的 wiki 頁 | 本頁首次出現的術語（v2 起新增）|
|---|---|---|---|---|---|---|
| 1 | 開場 | 電從哪裡來？馬達為什麼會轉？ | 電機就是在電能與機械能之間轉換的裝置 | 發電機：機械→電；電動機：電→機械；變壓器：換電壓 | concepts/electric-machines | 發電機、電動機、變壓器 |
| 2 | 開場 | 這份簡報的地圖 | 五章的順序與彼此關係 | 章節目錄（可點選跳轉）；故事線一句話 | index | — |
| 3 | Ch.1 | 一切都從磁場開始：四大原理 | 四個原理分別是誰的基礎 | 電流產生磁場；磁通變化感應電壓（變壓器，法拉第定律）；電流受力（電動機）；導線運動產生電壓（發電機） | concepts/four-magnetic-principles、concepts/faraday-law | 磁通、法拉第定律 |
| 4 | Ch.1 | 為什麼電機都用鐵心？ | 鐵比空氣容易導磁幾千倍；磁路像電路 | $\mu_r$ 約 2000～6000；磁動勢 $Ni$ 推磁通、磁阻擋磁通；磁路與電路對照 | concepts/magnetic-field-and-permeability、concepts/magnetic-circuit | 相對導磁係數、磁動勢、磁阻、磁路 |
| 5 | Ch.1 | 例題引導：一小段空氣有多麻煩？ | 用磁路算出氣隙磁阻是鐵心的近 5 倍 | 例 1-2 分 4 步：串聯 → 鐵心磁阻 66,300 → 氣隙磁阻 316,000 → 電流 0.602 A | examples/ch01-air-gap | 真空導磁係數 $\mu_0$、串聯、轉子、定子 |
| 6 | Ch.1 | 同一根棒子，推它發電、拉它變馬達 | 同一台機器可當發電機也可當電動機 | 線性直流機；拉（負載）→ 變慢、電動機；推 → 變快、發電機；啟動電流很大 | concepts/linear-dc-machine、examples/ch01-linear-machine | 無載、啟動電流 |
| 7 | Ch.2 | 為什麼需要變壓器？ | 高壓輸電能大幅降低損失 | 12～25 kV 發電 → 升壓 110 kV 以上 → 降壓配電 → 120 V；例 2-1 損失 1484 W → 16.7 W | concepts/transformer、examples/ch02-transmission | 輸電、配電 |
| 8 | Ch.2 | 理想變壓器：電壓變、功率不變 | 電壓比 $a$、電流比 $1/a$ | 兩線圈共用磁通；$V_P/V_S = a$、$I_P/I_S = 1/a$；功率相等；阻抗乘 $a^2$ | concepts/ideal-transformer、concepts/faraday-law | 一次／二次繞組、匝數比、相角、阻抗 |
| 9 | Ch.2 | 真實的變壓器不完美 | 漏磁、激磁電流、損失可以畫成等效電路 | 漏磁 → 漏電抗；建立磁通 → $X_M$；鐵損 → $R_C$；繞組 → 電阻；開路/短路測試量參數 | concepts/real-transformer、concepts/transformer-equivalent-circuit、concepts/oc-sc-test | 電抗、漏磁通、磁化電流、激磁電流／激磁支路、額定、開路／短路測試 |
| 10 | Ch.3 | 轉動的線圈＝交流發電機 | 交流電是線圈在磁場中轉出來的 | $e = \phi_{max}\omega\sin\omega t$；電壓取決於磁通、轉速、構造 | concepts/rotating-loop、concepts/ac-induced-voltage | 交流電、三相 |
| 11 | Ch.3 | 旋轉磁場：交流馬達的祕密 | 三相電流能產生大小不變、會轉的磁場 | 三組相隔 120° 的線圈；合成磁場大小 $1.5B_M$；對調兩相就反轉 | concepts/rotating-magnetic-field | 定子、轉子（再次說明）、旋轉磁場 |
| 12 | Ch.3 | 磁極越多，轉得越慢 | 用 $n = 120f/P$ 算轉速 | 60 Hz：2 極 3600、4 極 1800 r/min；$P$ 是極數不是極對數 | concepts/electrical-frequency-and-speed | 極數、r/min |
| 13 | Ch.4 | 同步發電機：動 → 電 | 發電機的電壓由場電流與轉速決定 | 轉子是電磁鐵、原動機帶著轉；$E_A = K\phi\omega$；轉速與頻率鎖定 | concepts/synchronous-generator、concepts/internal-generated-voltage | 場電流、原動機、內生電壓 |
| 14 | Ch.4 | 接上負載後，電壓為什麼會變？ | 同步電抗造成壓降；功因決定電壓升或降 | $V_\phi = E_A - jX_SI_A$；例 4-3：同樣 $E_A$，落後 410 V、單位 468 V、超前 535 V | concepts/synchronous-equivalent-circuit、concepts/generator-operating-alone、examples/ch04-power-factor | 電樞反應、同步電抗、功率因數、落後、超前 |
| 15 | Ch.5 | 同步電動機：同一台機器反過來 | 發電機與電動機的差別只在功率方向 | 轉子追著旋轉磁場；$E_A$ 領先＝發電機、落後＝電動機；轉速固定；脫出轉矩 | concepts/synchronous-motor、concepts/synchronous-motor-torque-speed | 轉矩角、速度調整率、脫出轉矩 |
| 16 | Ch.5 | 例題引導：轉一顆旋鈕，省下 28% 損失 | 過激同步電動機能供給虛功率、改善功因 | V 曲線；例 5-3 分 3 步：$Q = P\tan\theta$ → 功因 0.812 → 0.957 → 電流 667 → 566 A | concepts/v-curve、concepts/power-factor-correction、examples/ch05-power-factor-correction | 實功率、虛功率、功因、單位功因、欠激、過激、感應電動機 |
| 17 | 收尾 | 一張圖串起全部 | 五章的關係 | 四大原理 → 變壓器 / 旋轉磁場 → 同步發電機 ⇄ 同步電動機 | concepts/four-magnetic-principles、各章樞紐頁 | — |
| 18 | 收尾 | 自我檢測 | 檢查自己是否理解 | 5 題選擇題，點選看答案與對應 wiki 頁 | 各題標註 | — |
