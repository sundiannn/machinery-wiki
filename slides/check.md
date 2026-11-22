# 簡報逐頁檢查紀錄

> 每一輪檢查新增一個區塊，不覆蓋舊的（見 AGENTS.md 第 5.4 節步驟 C）。
> 不通過的頁面只重生該頁；同一頁重生 3 次仍不通過，停下來問使用者。
> 檢查者：另一個沒有參與製作的 AI（子代理），只拿到 `wiki/` 與 `slides/index.html`，看不到講義、log 與大綱。

## 第 1 輪（2026-11-23，檢查 v1）

| 頁 | 依據的 wiki 頁 | 事實可追溯 | 新手看得懂 | 結果 | 修正內容 |
|---|---|---|---|---|---|
| 1 | concepts/electric-machines.md | ✅ | ✅ | 通過 | — |
| 2 | index.md | ✅ | ✅ | 通過 | — |
| 3 | concepts/four-magnetic-principles.md、concepts/faraday-law.md | ❌ | ✅ | 重生 | 結論框「是磁通的『變化』才會產生電壓，**磁場再強**、只要不變就沒有電壓」把 wiki 的「磁通」改寫成「磁場」，意思變了。faraday-law.md 原文是「重點在『變化』：**磁通再大**，只要不變，就不會感應出電壓」。改成「磁場」後，與同一頁的原理④「導線在磁場中移動，兩端就有電壓」直接矛盾（④ 的磁場是不變的，卻有電壓），新手會被誤導。修正：改為「對靜止的線圈來說，是**穿過線圈的磁通**『變化』才會產生電壓；磁通再大，只要不變就沒有電壓（原理④是導線自己在動，是另一種情況）」。（另：③④的公式 $F = ilB\sin\theta$、$e=(\mathbf v\times\mathbf B)\cdot\mathbf l$ 只出現在連結頁 concepts/induced-force.md、concepts/motional-voltage.md，可追溯，但建議把這兩頁加進 data-src，見次要建議。） |
| 4 | concepts/magnetic-field-and-permeability.md、concepts/magnetic-circuit.md | ✅ | ✅ | 通過 | —（公式符號說明見次要建議） |
| 5 | examples/ch01-air-gap.md | ✅ | ❌ | 重生 | ① 推論跳步：步驟 2、3 算出 66,300 與 316,000，步驟 4 突然出現 $\mathfrak{R}_{eq}=382{,}300$，沒有「相加」這一步。wiki 有獨立的步驟 4「串聯相加…$\mathfrak{R}_{eq} = 66{,}300 + 316{,}000 = 382{,}300$」，也有步驟 5「$\phi = BA$，要用**氣隙**的有效面積」。修正：在步驟 3、4 之間補「串聯磁阻直接相加：$\mathfrak{R}_{eq}=66{,}300+316{,}000=382{,}300$」，並在步驟 4 加一句「磁通 $\phi = BA$，$A$ 用氣隙面積 12.6 cm²；再由 $Ni=\phi\mathfrak{R}_{eq}$ 求 $i$」。② 未解釋的常數：$4\pi\times10^{-7}$ 在本頁與前頁都沒說明。修正：加註「$\mu_0 = 4\pi\times10^{-7}$ H/m 是真空（空氣）的導磁係數，鐵心的 $\mu = \mu_r\mu_0$」（magnetic-field-and-permeability.md 有此式）。③ 結論句「所以**轉子與定子**間的氣隙要越小越好」：「轉子」「定子」在整份簡報都沒有定義（第一次出現在這頁）。修正：加括號「轉子（會轉的部分）與定子（不動的外殼）」，定義見 concepts/ac-machines.md「會轉動的部分叫轉子，靜止的部分叫定子」。 |
| 6 | concepts/linear-dc-machine.md、examples/ch01-linear-machine.md | ✅ | ✅ | 通過 | — |
| 7 | concepts/transformer.md、examples/ch02-transmission.md | ✅ | ✅ | 通過 | — |
| 8 | concepts/ideal-transformer.md、concepts/faraday-law.md | ✅ | ❌ | 重生 | 兩個重點條目用了沒解釋過的術語：「只改變大小，**不改變相角**」與「從一次側看，負載**阻抗**變成 $a^2$ 倍」。高中物理沒有「相角」「阻抗」，前面 7 頁也都沒提。另外圖中「一次繞組／二次繞組」沒說哪一邊接電源。修正：(a)「一次繞組（接電源的那組）、二次繞組（接負載的那組）」（transformer.md：「接電源的叫一次繞組…接負載的叫二次繞組」）；(b)「阻抗」加括號「交流電路裡『阻礙電流』的程度，可想成交流版的電阻」；(c)「相角」改成白話「電壓、電流波形的『步調』（何時到達最高點）不會被錯開」，或若不打算解釋就刪掉這一條。 |
| 9 | concepts/real-transformer.md、concepts/transformer-equivalent-circuit.md、concepts/oc-sc-test.md | ✅ | ❌ | 重生 | 對新手術語過密且未解釋：(a)「**電抗**」（漏電抗、磁化電抗）從未定義；(b)「**激磁支路**」與「**激磁電流**」突然出現，表格裡講的是「磁化電流」與「鐵心發熱」，沒有說激磁電流＝兩者合起來（real-transformer.md：「激磁電流…由兩部分組成：磁化電流 $i_M$、鐵損電流 $i_{h+e}$」），新手接不起來；(c)「**額定**電壓／額定電流」未解釋；(d)「串聯阻抗」中的「阻抗」若第 8 頁未補定義也會卡住。修正：在表格下加一行「激磁電流＝磁化電流＋鐵損電流，它走的兩個並聯元件合稱『激磁支路』」；「電抗」加括號「線圈對交流電的阻礙，像電阻但不發熱」；「額定」加括號「設備設計時規定的正常使用值」。 |
| 10 | concepts/rotating-loop.md、concepts/ac-induced-voltage.md | ✅ | ✅ | 通過 | —（措辭小問題見次要建議） |
| 11 | concepts/rotating-magnetic-field.md | ✅ | ❌ | 重生 | 本頁核心句「**定子**磁場在轉，**轉子**磁場就會一直『追著』它轉」依賴「定子／轉子」，但整份簡報從未定義（第 5 頁也只是直接使用）。另「大小永遠是 $1.5B_M$」中的 $B_M$ 沒有說明是什麼。修正：(a) 在第一條前加「電機分成不動的**定子**和會轉的**轉子**」（concepts/ac-machines.md：「會轉動的部分叫轉子（rotor），靜止的部分叫定子（stator）」；建議同時把 ac-machines.md 加進 data-src）；(b) 加註「$B_M$＝單一線圈磁場的最大值」（rotating-magnetic-field.md：「$B_M$ 單一線圈磁通密度的峰值」），或改寫為「大小固定，是單一線圈最大磁場的 1.5 倍」。 |
| 12 | concepts/electrical-frequency-and-speed.md | ✅ | ✅ | 通過 | — |
| 13 | concepts/synchronous-generator.md、concepts/internal-generated-voltage.md | ✅ | ❌ | 重生 | 本頁結論「調電壓的旋鈕只剩一個：**轉子的場電流**」——「場電流」一詞在本頁與前頁都沒有定義，第一條只說「轉子通直流電」，新手不知道兩者是同一件事；而第 14、16 頁又以「場電流」為主角。修正：第一條改為「轉子線圈通**直流電（叫做『場電流』）**，變成一塊電磁鐵」（synchronous-generator.md：「場繞組：產生主磁場的繞組…同步電機的場繞組在轉子上」；internal-generated-voltage.md：「磁通又取決於轉子場電流 $I_F$」），並在 $E_A$ 下補一句「場電流越大 → 電磁鐵越強（磁通越大）→ $E_A$ 越大」，把「場電流→磁通→電壓」的因果鏈接起來。 |
| 14 | concepts/synchronous-equivalent-circuit.md、concepts/generator-operating-alone.md、examples/ch04-power-factor.md | ✅ | ❌ | 重生 | ① 未解釋的術語：「**功率因數**（功因）」「電感性（**落後**）」「電容性（**超前**）」「電樞」「$V_\phi$」「$R_A$」及方程式中的 $j$ 與粗體相量，整份簡報之前都沒出現過；$\mathbf{V}_\phi = \mathbf{E}_A - jX_S\mathbf{I}_A - R_A\mathbf{I}_A$ 對高中程度讀者無法閱讀。② 例題數字的呈現會誤導：圖上方寫「$E_A$ 固定 277 V」，長條卻是 410／468／535 V，新手會以為「端電壓比內生電壓還高」，與本頁「落後負載讓電壓明顯下降」相衝突。實際上 wiki（examples/ch04-power-factor.md）：「$E_A = V_\phi = 480/\sqrt3 \approx 277$ V」是**每相**電壓，而 410 V 等是「Y 接：$V_T = \sqrt3 \times 236.8 = 410$ V」的**線間端電壓**，且無載時端電壓是 480 V。修正：(a) 長條圖改為與「無載 480 V」比較（加一條 480 V 參考線），標題改成「無載時端電壓 480 V；接上 60 A 負載後」，不要把每相 277 V 放在旁邊比；或全部改用每相值 236.8／270.4／308.8 V 對照 277 V；(b) 加一個方塊白話說明：「功率因數：負載真正用掉的功率佔比；馬達這類線圈型負載電流『慢半拍』叫落後，電容型負載電流『搶先』叫超前」（generator-operating-alone.md 有「馬達、冷氣這類『電感性』負載（落後功因）」）；(c) 方程式改為白話「端電壓 = 內生電壓 − 同步電抗造成的壓降 − 線圈電阻壓降」，原式可縮小放在註腳。 |
| 15 | concepts/synchronous-motor.md、concepts/synchronous-motor-torque-speed.md | ✅ | ❌ | 重生 | 對照表第一列「$\mathbf{E}_A$ 與 $\mathbf{V}_\phi$：$\mathbf{E}_A$ 領先／$\mathbf{E}_A$ 落後」需要相量觀念，新手無從理解；「**轉矩角 $\delta$**」在第二個重點突然出現，沒有和第一段「保持一個角度」連起來；「感應轉矩」「速度調整率」也未解釋。修正：(a) 第一段改為「…永遠追不上，兩者之間保持一個角度（叫**轉矩角 $\delta$**），負載越重角度越大」（synchronous-motor-torque-speed.md：「負載變重時，轉子只是稍微『往後退』一點（轉矩角變大）」）；(b) 表格第一列改為白話「轉子磁場在淨磁場的前面（發電機）／後面（電動機）」（synchronous-motor.md：「發電機：$\mathbf{B}_R$ 領先 $\mathbf{B}_{net}$…電動機：$\mathbf{B}_R$ 落後」），$E_A$/$V_\phi$ 的說法移到註腳；(c)「速度調整率 0%」後加「（負載從無到滿，轉速變化 0%）」。 |
| 16 | concepts/v-curve.md、concepts/power-factor-correction.md、examples/ch05-power-factor-correction.md | ✅ | ❌ | 重生 | 本頁大量未定義術語與跳步：「**虛功率**」「kVAR」「單位功因」「電樞電流」「**感應電動機**」（整份簡報從未介紹）「$\tan\theta$ 的 $\theta$」。步驟 1「已知 $P$ 和功因，$Q = P\tan\theta$」對新手是憑空出現的公式，wiki 有推導「$Q = S\sin\theta = \dfrac{P}{\cos\theta}\sin\theta = P\tan\theta$」以及「功因 $=\cos\theta$」。修正：(a) 加一個白話框：「實功率 $P$＝真正被用掉的功率（kW）；虛功率 $Q$＝在電線上來回搬運卻沒被用掉的功率（kVAR），它一樣會讓電線電流變大、損失變多」（power-factor-correction.md 白話解釋）；「功因＝$\cos\theta$，$\theta$ 是電壓與電流錯開的角度，功因 1 叫單位功因」；(b)「感應電動機」加括號「工廠最常見的一種交流馬達，功因落後」（power-factor-correction.md：「典型電力系統的負載大多是感應電動機…幾乎都是落後功因」）；(c) 步驟 1 補上推導或至少說明 $\theta=\cos^{-1}(\text{功因})$。 |
| 17 | concepts/four-magnetic-principles.md、concepts/transformer.md、concepts/ac-machines.md、concepts/synchronous-generator.md、concepts/synchronous-motor.md | ✅ | ✅ | 通過 | —（建議見次要建議） |
| 18 | concepts/transformer.md、concepts/magnetic-circuit.md、concepts/electrical-frequency-and-speed.md、concepts/synchronous-motor-torque-speed.md、concepts/v-curve.md | ✅ | ✅ | 通過 | —（已核對 5 題的 `data-answer` 均為正確選項：B、C、A、B、C） |

### 次要建議（不影響通過）

1. **第 3 頁 data-src**：原理③④的公式 $F = ilB\sin\theta$、$e = (\mathbf v\times\mathbf B)\cdot\mathbf l$ 實際出處是 concepts/induced-force.md 與 concepts/motional-voltage.md（four-magnetic-principles.md 只有文字敘述），建議加入 data-src，讓 📖 直接連到公式出處。$e=-N\,d\phi/dt$ 的微分符號可加一句「$d\phi/dt$＝磁通變化的快慢」。
2. **第 4 頁**：磁阻 $\mathfrak{R} = l/(\mu A)$ 中的 $l$、$\mu$、$A$ 沒有說明；建議加「$l$：路徑長、$A$：截面積、$\mu$：導磁係數（鐵心的 $\mu=\mu_r\mu_0$）」，也可加一句 wiki 的水管比喻（magnetic-circuit.md：「氣隙則像一段很細的管子」）。
3. **第 5 頁 SVG**：長度長條鐵心 280 px、氣隙 2 px（約 1/140），標籤寫 1/800；屬示意可接受，可加註「（不按比例）」。
4. **第 6 頁**：文字提到「合上開關」，但示意圖沒有畫開關與電阻（linear-dc-machine.md：「電池、電阻經開關接到兩條…軌道」）；「無載」一詞建議加括號「（沒有外力推拉）」。
5. **第 7 頁**：「電流變 1/10」實際數字為 90.8 → 9.594 A（約 1/9.5），可改為「電流約變成 1/10」。
6. **第 10 頁**：「任何真實發電機的電壓都**只**取決於三件事」比 wiki 多了「只」字（rotating-loop.md：「任何真實電機的電壓都取決於三件事：磁通、轉速、構造」），建議刪「只」。$\phi_{max}$ 可加註「線圈正對磁場時穿過的最大磁通」。
7. **第 14 頁**：「468 V」wiki 為 468.4 V，四捨五入可接受。
8. **第 17 頁**：「Ch.1 線性直流機」一格的出處 concepts/linear-dc-machine.md 未列入 data-src（只能經由 four-magnetic-principles.md 的連結追溯），建議加入。「內生電壓領先／落後端電壓」若第 15 頁照建議改寫，這裡也宜同步改為「轉子磁場在前／在後」。
9. **第 18 頁**：第 2 題解析引用「近 5 倍」，此數字只在 examples/ch01-air-gap.md，📖 建議改指該例題頁（magnetic-circuit.md 只寫「氣隙比鐵心短 800 倍，卻貢獻大部分磁阻」）。
10. **全份**：建議在第 2 頁地圖或第 11 頁前放一個極簡「名詞小抄」（定子、轉子、場電流、功率因數、虛功率），可一次解決第 5、11、13、14、16 頁的術語問題。

### 本輪統計
通過：9 頁（1、2、4、6、7、10、12、17、18）；重生：9 頁（3、5、8、9、11、13、14、15、16）

## 第 2 輪（2026-11-23，檢查 v2：重生第 3、5、8、9、11、13～16 頁後）

> 由另一個新的子代理執行（沒有看過第 1 輪報告）。

| 頁 | 依據的 wiki 頁 | 事實可追溯 | 新手看得懂 | 結果 | 修正內容 |
|---|---|---|---|---|---|
| 1 | concepts/electric-machines.md | ✅ | ✅ | 通過 | — |
| 2 | index.md | ✅ | ✅ | 通過 | — |
| 3 | four-magnetic-principles、faraday-law、induced-force、motional-voltage | ✅ | ✅ | 通過 | —（見次要建議 1） |
| 4 | magnetic-field-and-permeability、magnetic-circuit | ✅ | ✅ | 通過 | —（見次要建議 2） |
| 5 | examples/ch01-air-gap、magnetic-field-and-permeability | ✅ | ✅ | 通過 | —（見次要建議 3） |
| 6 | linear-dc-machine、examples/ch01-linear-machine | ✅ | ✅ | 通過 | —（見次要建議 4） |
| 7 | transformer、examples/ch02-transmission | ✅ | ✅ | 通過 | — |
| 8 | ideal-transformer、faraday-law、beginner-glossary | ✅ | ✅ | 通過 | — |
| 9 | real-transformer、transformer-equivalent-circuit、oc-sc-test、beginner-glossary | ✅ | ✅ | 通過 | —（見次要建議 5） |
| 10 | rotating-loop、ac-induced-voltage | ✅ | ✅ | 通過 | —（見次要建議 6） |
| 11 | rotating-magnetic-field、ac-machines | ✅ | ✅ | 通過 | —（見次要建議 7） |
| 12 | electrical-frequency-and-speed | ✅ | ✅ | 通過 | — |
| 13 | synchronous-generator、internal-generated-voltage | ✅ | ✅ | 通過 | —（見次要建議 8） |
| 14 | synchronous-equivalent-circuit、generator-operating-alone、examples/ch04-power-factor、beginner-glossary | ✅ | ❌ | 重生 | **(1) 文字公式和自己的例題結果互相矛盾。** 投影片寫「端電壓 ＝ 內生電壓 − 同步電抗造成的壓降 − 線圈電阻的壓降」。新手會照字面當成一般的減法，推出「端電壓一定比內生電壓小」。但同一頁的長條圖卻顯示 0.8 超前時是 535 V，比無載的 480 V 還高，新手無法理解。wiki（synchronous-equivalent-circuit）的式子是相量式 $\mathbf{V}_\phi = \mathbf{E}_A - jX_S\mathbf{I}_A - R_A\mathbf{I}_A$；generator-operating-alone 的表格寫「超前（−Q，電容性）→ **上升**」。建議改成：「端電壓 ＝ 內生電壓 再扣掉同步電抗與線圈電阻造成的電壓變化。這個『扣』要考慮電流和電壓的步調，所以結果可能變小（落後），也可能變大（超前）。」**(2)「單位功因」「0.8 落後／0.8 超前」比定義先出現。** 本頁只把功因解釋成「電流和電壓步調差多少」，沒說功因是 0～1 的數字，也沒說什麼是「單位功因」。這兩個詞直到第 16 頁才定義（「功因 $= \cos\theta$……功因 1 叫單位功因」），本頁的長條圖標籤卻已經在用。依據 beginner-glossary：「**功率因數（功因）**：$\cos\theta$，$\theta$ 是電壓與電流錯開的角度；功因 1 稱為單位功因」。建議在本頁的功因說明後補一句：「功因用 0～1 的數字表示（$=\cos\theta$）：1 叫**單位功因**，表示步調完全一致；0.8 表示錯開了一些。」並把第 16 頁的同一句改成回顧。**(3)「電感」在全份簡報中沒有解釋過**（「加上線圈的電感」「電感性負載」）。建議改成「加上線圈本身的電抗（第 9 頁）」，或補一句「電感：線圈阻礙電流變化的特性」。 |
| 15 | synchronous-motor、synchronous-motor-torque-speed | ❌ | ❌ | 重生 | **(1) 轉矩角的定義和 wiki 不符。** 投影片寫「定子通三相電 → 旋轉磁場；轉子電磁鐵被它拉著……轉子永遠追不上，兩者之間保持一個角度，叫轉矩角 $\delta$」，這裡的「兩者」是轉子和定子的旋轉磁場。wiki 的定義是 $\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ 的夾角：synchronous-equivalent-circuit（由 synchronous-motor 直接連到）寫「$\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ 的夾角稱為**內角**或**轉矩角** $\delta$」，beginner-glossary 寫「**轉矩角 $\delta$**：轉子磁場與淨磁場之間的夾角」。而且同一頁的表格又寫「轉子磁場在**淨磁場**的前面／後面」，前後所說的角度對象不一致。**(2)「淨磁場」沒有定義**，第 1～14 頁都沒出現過。建議把第一段改成：「定子通三相電 → 旋轉磁場；轉子電磁鐵被它拉著，以完全相同的速度旋轉。定子磁場和轉子磁場加起來叫**淨磁場**；當電動機時，轉子磁場永遠落在淨磁場後面一個角度，這個角度叫**轉矩角 $\delta$**——負載越重，角度越大。」依據：synchronous-equivalent-circuit「淨磁場 $\mathbf{B}_{net} = \mathbf{B}_R + \mathbf{B}_S$」；synchronous-motor「電動機：$\mathbf{B}_R$ 落後」「轉矩角增大，轉矩跟著增大，直到等於負載轉矩」。同時建議把 beginner-glossary 加進 data-src。**(3)「轉矩」第一次出現，沒有說明。** 建議第一次出現時加括號：「轉矩（讓東西轉動的力，也就是高中的『力矩』）」。 |
| 16 | v-curve、power-factor-correction、examples/ch05-power-factor-correction、ac-power、beginner-glossary | ✅ | ✅ | 通過 | —（見次要建議 9；若第 14 頁照建議補上功因定義，本頁第二段可改成回顧） |
| 17 | four-magnetic-principles、linear-dc-machine、transformer、ac-machines、synchronous-generator、synchronous-motor | ✅ | ✅ | 通過 | — |
| 18 | transformer、examples/ch01-air-gap、electrical-frequency-and-speed、synchronous-motor-torque-speed、v-curve | ✅ | ✅ | 通過 | — |

### 次要建議（不影響通過）

1. **第 3 頁**：$F = ilB\sin\theta$ 的 $\theta$，以及 $e = (\mathbf{v}\times\mathbf{B})\cdot\mathbf{l}$ 的向量外積、內積，都沒有說明。建議補一句「$\theta$：導線與磁場的夾角」（induced-force：「$\theta$ 導線與磁通密度的夾角」）。原理④可以加注「最簡單的情況（三者互相垂直）就是 $e = vBl$」（motional-voltage 例 1-8：5 m/s、0.5 T、1 m → 2.5 V）。
2. **第 4 頁**：磁阻 $\mathfrak{R} = \dfrac{l}{\mu A}$ 裡的 $l$、$\mu$、$A$ 沒有說明，$\mu$ 要到第 5 頁才解釋。建議在表下補「$l$：磁路長度、$A$：截面積、$\mu$：材料的導磁係數」（magnetic-circuit 符號表）。
3. **第 5 頁**：「轉子（會轉的部分）與定子（不動的部分）」的定義，在本頁 data-src（ch01-air-gap、magnetic-field-and-permeability）及其直接連結裡都找不到，只寫在 beginner-glossary 和 ac-machines。內容本身正確，建議把 `concepts/beginner-glossary.md` 加進本頁的 data-src。
4. **第 6 頁**：「跑得越快，棒子自己產生的電壓越大、電流越小」少了一個原因。建議補「（棒子的電壓和電池方向相反，互相抵消）」，依據 linear-dc-machine：「電流 $i = (V_B - e_{ind})/R$ 變小」。
5. **第 9 頁**：短路測試求出的 $R_{eq}$、$X_{eq}$ 是新符號，表格裡只有 $R_P$、$R_S$、$X_P$、$X_S$。建議補「（兩側串聯電阻、電抗合起來的總值）」，依據 transformer-equivalent-circuit：「兩側的串聯阻抗直接相加成 $R_{eq} + jX_{eq}$」。
6. **第 10 頁**：$e = \phi_{max}\,\omega\sin\omega t$ 的符號沒有說明。建議補「$\phi_{max}$：穿過線圈的最大磁通；$\omega$：轉動的角速度」（rotating-loop 符號表），這樣也能直接對到下一行的「磁通、轉速」。
7. **第 11 頁**：「相位相差 120°」的「相位」和第 8 頁的「相角」用詞不同，建議統一成「相角（步調）」。
8. **第 13 頁**：$E_A = K\phi\omega$ 的 $K$ 沒有說明，建議補「$K$：由電機構造決定的常數」（internal-generated-voltage）。
9. **第 16 頁**：步驟 2、3 直接給出「功因 0.812」「線電流 667 A」，沒寫算法。可加一行小字「功因 $= \cos(\tan^{-1}\frac{Q}{P})$」（examples/ch05-power-factor-correction 步驟 3）；線電流的 $\sqrt3$ 公式可以只寫「由功率與電壓算出」，避免新手卡住。

### 本輪統計

- 通過：16 頁（1、2、3、4、5、6、7、8、9、10、11、12、13、16、17、18）
- 重生：2 頁（14、15）

## 第 3 輪（2026-11-23，檢查 v3：重生第 14、15 頁後）

> 由另一個新的子代理執行（沒有看過前兩輪報告）。

| 頁 | 依據的 wiki 頁 | 事實可追溯 | 新手看得懂 | 結果 | 修正內容 |
|---|---|---|---|---|---|
| 1 | concepts/electric-machines.md | ✅ | ✅ | 通過 | 無。「發電機 機械→電」「電動機 電→機械」「變壓器 把交流電換成另一個電壓」都和 wiki〔講義 p.1〕相符。「渦輪轉動」可由 electric-machines.md 直接連結的 synchronous-generator.md（「渦輪帶著轉子轉」）支持。「同一套原理」對應「三種裝置靠的都是磁場四大原理」。 |
| 2 | index.md | ✅ | ✅ | 通過 | 無。這頁是導覽，五章標題和 index.md 的章節結構一致。 |
| 3 | four-magnetic-principles、faraday-law、induced-force、motional-voltage | ✅ | ✅ | 通過 | 無。$e=-N\,d\phi/dt$、$F=ilB\sin\theta$（「θ：導線與磁場的夾角」）、四個原理分別對應「變壓器／電動機／發電機」作用，都和 wiki 相符。$e=vBl$ 是 motional-voltage.md 向量式在三者互相垂直時的結果，直接連結的 linear-dc-machine.md 也寫了 $e_{ind}=vBl$。「磁通再大，只要不變就沒有電壓」和 faraday-law.md 的白話解釋一致。 |
| 4 | magnetic-field-and-permeability、magnetic-circuit | ✅ | ✅ | 通過 | 無。「2000～6000 倍」和 wiki「鋼中建立的磁通是空氣的 2000～6000 倍」一致。電路與磁路對照表、$\mathfrak{F}=Ni$、$\mathfrak{R}=l/(\mu A)$、$\mathfrak{F}=\phi\mathfrak{R}$ 都和 magnetic-circuit.md 一致。SVG 標了「線圈 N 匝」與「氣隙」，也註明「示意圖，AI 繪製」。 |
| 5 | examples/ch01-air-gap、magnetic-field-and-permeability、beginner-glossary | ✅ | ✅ | 通過 | 無。40 cm、0.05 cm、12 cm²、μr=4000、400 匝、多 5%（12.6 cm²）、66,300、316,000、382,300、0.602 A 都和例題頁逐項相符。SVG 的「≈ 4.8 倍」是 316,000/66,300≈4.77 算出來的，和 wiki「將近 5 倍」一致。轉子、定子在頁內就有解釋。 |
| 6 | concepts/linear-dc-machine、examples/ch01-linear-machine | ✅ | ✅ | 通過 | 無。120、129、111 m/s，30 N，400 A，30 A，以及「推是發電機變快、拉是電動機變慢」都和例 1-10 相符。「棒子自己產生的電壓和電池方向相反、互相抵消，所以電流越小」對應 $i=(V_B-e_{ind})/R$。 |
| 7 | concepts/transformer、examples/ch02-transmission | ✅ | ✅ | 通過 | 無。12～25 kV、110 kV～近 1000 kV、12～34.5 kV、120 V，以及 90.8/9.594 A、454/479.7 V、1484/16.7 W、「約 1/89」都和 wiki 一致。「頻率不變」「理想上不改變傳送的功率」也有出處。 |
| 8 | ideal-transformer、faraday-law、beginner-glossary | ✅ | ✅ | 通過 | 無。$V_P/V_S=N_P/N_S=a$、$I_P/I_S=1/a$、功率守恆、相角不變、阻抗變 $a^2$ 倍都和 ideal-transformer.md 相符。「相角」「阻抗」在頁內有白話解釋，和 glossary 一致。 |
| 9 | real-transformer、transformer-equivalent-circuit、oc-sc-test、beginner-glossary | ✅ | ✅ | 通過 | 無。四個非理想效應分別對應 $R_P,R_S$／$X_P,X_S$（串聯）、$X_M$／$R_C$（並聯激磁支路），和等效電路頁的表一致。開路測試加額定電壓、求 $R_C,X_M$；短路測試低壓側短路、調到額定電流、求 $R_{eq},X_{eq}$，都和 oc-sc-test.md 一致。「電抗」「額定」「激磁電流」都先解釋才使用。 |
| 10 | rotating-loop、ac-induced-voltage | ✅ | ✅ | 通過 | 無。$e=\phi_{max}\omega\sin\omega t$、「兩條邊輪流切過磁場」、「磁通、轉速、構造」三件事都和 rotating-loop.md 相符。三組線圈錯開 120° 得到三相電壓，對應 ac-induced-voltage.md 的 $e_{bb'}$、$e_{cc'}$。SVG 的波形是「轉一圈＝一個完整週期」，和 wiki「轉一圈，就產生一個完整的正弦波電壓」一致。 |
| 11 | rotating-magnetic-field、ac-machines | ✅ | ✅ | 通過 | 無。相隔 120°、電流相差 120°、每個線圈磁場方向固定、合成大小為 1.5 倍並且旋轉、任意兩相對調就反轉、「所有交流電動機的基本原理」，都和 wiki 逐項相符。 |
| 12 | electrical-frequency-and-speed | ✅ | ✅ | 通過 | 無。$n_{sm}=120f_{se}/P$、3600／1800 r/min、「同樣的 N-S 花紋重複兩次」、「P 是極數不是極對數」都和 wiki 一致。 |
| 13 | synchronous-generator、internal-generated-voltage | ✅ | ✅ | 通過 | 無。轉子通直流電（場電流）成為電磁鐵、原動機、$n=120f/P$、$E_A=K\phi\omega$（K 由構造決定），以及「轉速必須固定，所以調電壓的旋鈕只剩場電流」都和 wiki 相符。 |
| 14 | synchronous-equivalent-circuit、generator-operating-alone、examples/ch04-power-factor、beginner-glossary | ✅ | ✅ | 通過 | 無。電樞反應加上線圈電抗合起來是 $X_S$（wiki：$X_S=X+X_A$）；端電壓由內生電壓扣掉 $jX_SI_A$ 與 $R_AI_A$ 而來；結果可能變小，也可能變大。功因＝cosθ、單位功因、電感性負載落後、電容性負載超前，都和 glossary 一致。410／468（wiki 468.4）／535 V、60 A、無載 480 V 都正確。長條圖高度（153／175／200）和 480 V 虛線位置都依比例畫，沒有誤導。「差了 125 V」是 535−410 算出來的。「（第 9 頁）」確實指向定義「電抗」的那一頁。 |
| 15 | synchronous-motor、synchronous-motor-torque-speed、synchronous-equivalent-circuit、rotational-motion、beginner-glossary | ✅ | ✅ | 通過 | 無。淨磁場＝定子磁場加轉子磁場；轉矩角是轉子磁場與淨磁場的夾角，負載越重越大；發電機「前面、轉矩方向相反」、電動機「後面、轉矩方向相同」；速度調整率 0%；δ=90° 時轉矩最大，約滿載的 3 倍；滑動極。以上都和 wiki 相符。「轉矩（扭力，高中的力矩）」來自 rotational-motion.md。「第 6 頁導體棒是同一個道理」可由 rotational-motion.md 直接連結的 linear-dc-machine.md 支持（「同樣的事在真實的交流同步電機上也成立」）。 |
| 16 | v-curve、power-factor-correction、examples/ch05-power-factor-correction、ac-power、beginner-glossary | ✅ | ✅ | 通過 | 無。欠激像電感、吸收 Q；過激像電容、供給 Q；V 形曲線；100 kW／0.78、200 kW／0.8、150 kW；80.2、150、93 kVAR；323.2→137.2 kVAR；0.812→0.957；667→566 A；約 28%；實功率不變。以上都和例 5-3 逐項相符。感應電動機「工廠最常見、功因落後」對應 power-factor-correction.md「工廠裡大多是功因落後的感應電動機」。 |
| 17 | four-magnetic-principles、linear-dc-machine、transformer、ac-machines、synchronous-generator、synchronous-motor | ✅ | ✅ | 通過 | 無。每個方塊的說明都有出處。「發電機轉子磁場在前、電動機在後」來自 synchronous-motor.md 的對照表（$\mathbf B_R$ 領先或落後），「同一台機器，功率方向相反」也和 wiki 一致。 |
| 18 | transformer、examples/ch01-air-gap、electrical-frequency-and-speed、synchronous-motor-torque-speed、v-curve | ✅ | ✅ | 通過 | 無。5 題的 `data-answer`（b、c、a、b、c）都是正確答案，解說也和各自的 wiki 頁一致。第 5 題解說中的「改善系統功因」可由 v-curve.md 直接連結的 power-factor-correction.md 支持。 |

### 次要建議（不影響通過）

1. **第 16 頁步驟 2**：原文「再由總功率與電壓算出線電流 667 A」沒有提到功因。步驟 3 的總功率（450 kW）和電壓（480 V）都沒變，電流卻從 667 A 變成 566 A，細心的新手可能會疑惑。建議改成「再由總功率、電壓**與功因**算出**輸電線電流** 667 A（功因越接近 1，電流越小）」。依據：例題頁 $I_L = \dfrac{450\text{ k}}{\sqrt3(480)(0.812)} = 667$ A。
2. **第 14 頁**：「端電壓」第一次出現時沒有說明。建議第一次出現時加註「端電壓（發電機輸出到外面的電壓）」，依據 synchronous-equivalent-circuit.md「輸出到外面的電壓 $V_\phi$」。另外「（$=\cos\theta$）」裡的 θ 在這頁沒有定義，第 3 頁的 θ 又是別的意思，建議寫成「$=\cos\theta$，θ 是電壓與電流錯開的角度」（glossary 原文）。
3. **第 3 頁**：$e=-N\,d\phi/dt$ 裡的 $N$ 在這頁沒有定義（第 4 頁 SVG 才寫「線圈 N 匝」）。建議補「$N$：線圈匝數」（faraday-law.md 符號表）。
4. **第 8 頁**：「同一個磁通變化，在每一匝感應出一樣的電壓（法拉第定律），所以：…$I_P/I_S=1/a$」。電流比並不是由法拉第定律推出的，wiki 的推導是 $N_P i_P = N_S i_S$。建議把電流比另起一句，寫成「兩側線圈的磁動勢互相抵消（$N_Pi_P=N_Si_S$），所以電流比反過來是 $1/a$」。
5. **第 5 頁**：「邊緣效應」沒有解釋。可以補一句「磁通在氣隙會向外擴散」（magnetic-circuit.md 原文）。
6. **第 9 頁**：「磁滯損＋渦流損」只出現名稱，可以接受，因為頁內已說明它們是「鐵心發熱」的原因。開路測試「電流只走激磁支路」和短路測試「只看到串聯的電阻與電抗」，wiki 原文都是「幾乎全部」，建議把「只」改成「幾乎只」，比較精確。
7. **第 6、15 頁**：「無載」「滿載」沒有定義。建議第一次出現時加註「無載（沒有外力或負載）」「滿載（額定負載）」。
8. **第 6 頁**：文字寫「合上開關」，但示意圖沒有畫開關。可以在圖上補一個開關符號，也可以把文字改成「接上電池」。

### 本輪統計

- 通過：18 頁
- 重生：0 頁

## 結論

- 3 輪檢查：9 頁重生 → 2 頁重生 → 0 頁重生，全部通過
- 每頁重生次數：第 14、15 頁各 2 次；第 3、5、8、9、11、13、16 頁各 1 次；其餘 0 次（皆未達 3 次上限）
- 第 3 輪後只採納 3 項次要建議的用字微調（第 3、9、16 頁），未再送檢，內容皆直接引自 wiki，見 log
