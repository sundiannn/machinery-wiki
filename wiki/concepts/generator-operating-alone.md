---
title: 發電機單獨運轉
en: Synchronous Generator Operating Alone
aliases: [發電機單獨運轉, 負載變化, 場電流調整, operating alone]
chapters: [ch04]
sources: [sources/ch04.md]
updated: 2026-11-23
status: draft
---

# 發電機單獨運轉（Synchronous Generator Operating Alone）

## 一句話說明
一台發電機自己供電時，加上不同功率因數的負載，端電壓的反應不同：**落後負載讓電壓明顯下降，超前負載反而讓電壓上升**；要穩住電壓就調場電流。

## 白話解釋
馬達、冷氣這類「電感性」負載（落後功因）會把發電機的電壓往下拉；電容性負載（超前功因）則會把電壓往上推。發電廠的做法是轉動「場電流」這顆旋鈕，讓電壓維持固定〔AI 補充〕。

## 正式內容
**假設**〔講義 p.20〕：忽略 $R_A$、轉速固定、除非明說，轉子磁通（$E_A$ 大小）固定。

**負載增加時**〔講義 p.20–21〕
- 同功因下加負載：$|\mathbf{I}_A|$ 變大但角度不變，所以 $jX_S\mathbf{I}_A$ 變長但方向不變；它必須連接角度 0° 的 $\mathbf{V}_\phi$ 和大小固定的 $\mathbf{E}_A$

| 加入的負載 | 端電壓 $V_\phi$、$V_T$ |
|---|---|
| 落後（+Q，電感性） | **明顯下降** |
| 單位功因（無虛功率） | 稍微下降 |
| 超前（−Q，電容性） | **上升** |

**電壓調整率**〔講義 p.21–22〕
- $\text{VR} = (V_{nl} - V_{fl})/V_{fl}\times100\%$
- 落後功因：相當大的正 VR；單位功因：小的正 VR；超前功因：常為負 VR

**如何補償端電壓變化**〔講義 p.22〕
- 頻率不能改，所以只能靠改變磁通來調整 $E_A = K\phi\omega$：
  1. 減小場電阻 → 場電流增加
  2. 場電流增加 → 磁通增加
  3. 磁通增加 → $E_A$ 增加
  4. $E_A$ 增加 → $V_\phi$ 與端電壓上升

**例題結論**
- 例 4-3：$E_A$ 固定 277 V 時，滿載 0.8 落後、單位功因、0.8 超前的端電壓分別為 410 V、468.4 V、535 V → [例題引導](../examples/ch04-power-factor.md)〔講義 p.26–30〕

## 和其他概念的關係
- 用的是[同步機等效電路](synchronous-equivalent-circuit.md)的相量圖
- VR 的定義與變壓器相同，見[電壓調整率與效率](voltage-regulation-and-efficiency.md)
- 落後／超前的意思見[交流功率](ac-power.md)
- 屬於[同步發電機](synchronous-generator.md)一章

## 出處
- [Ch.4 來源摘要](../sources/ch04.md)〔講義 p.20–30〕
