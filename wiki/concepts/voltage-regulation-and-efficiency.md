---
title: 電壓調整率與效率
en: Voltage Regulation and Efficiency
aliases: [電壓調整率, 效率, VR, 相量圖, voltage regulation, efficiency, phasor diagram]
chapters: [ch02, ch03]
sources: [sources/ch02.md, sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 電壓調整率與效率（Voltage Regulation and Efficiency）

## 一句話說明
**電壓調整率**看「接上負載後輸出電壓掉了多少」，**效率**看「輸入的功率有多少真的送出去」。

## 白話解釋
家裡同時開很多電器時燈會稍微變暗，因為變壓器內部的阻抗讓輸出電壓下降；電壓調整率就是在量這個「掉多少」。效率則是「沒變成熱浪費掉」的比例〔AI 補充〕。

## 正式內容
**電壓調整率（VR）**〔講義 p.34〕
實際變壓器內有串聯阻抗，即使輸入電壓固定，輸出電壓也會隨負載改變。

$$ \text{VR} = \frac{V_{S,nl} - V_{S,fl}}{V_{S,fl}}\times100\% = \frac{V_P/a - V_{S,fl}}{V_{S,fl}}\times100\% $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $V_{S,nl}$ | 二次側無載電壓（$= V_P/a$） | V |
| $V_{S,fl}$ | 二次側滿載電壓 | V |

**相量圖與功因的影響**〔講義 p.35–36〕
以 $\mathbf{V}_S$ 為 0° 參考，由近似等效電路的 KVL：

$$ \frac{\mathbf{V}_P}{a} = \mathbf{V}_S + R_{eq}\mathbf{I}_S + jX_{eq}\mathbf{I}_S $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $R_{eq}, X_{eq}$ | 轉換到二次側的等效電阻與電抗 | Ω |
| $\mathbf{I}_S$ | 二次側電流相量 | A |

| 負載功因 | 結果 |
|---|---|
| 落後（lagging） | $V_P/a > V_S$，VR > 0，而且最大 |
| 單位功因 | VR > 0，但比落後時小 |
| 超前（leading） | $V_S$ 可能高於 $V_P/a$，VR 可能**小於 0** |

**效率**〔講義 p.36〕

$$ \eta = \frac{P_{out}}{P_{in}}\times100\% = \frac{P_{out}}{P_{out}+P_{loss}}\times100\% = \frac{V_S I_S\cos\theta}{P_{Cu} + P_{core} + V_S I_S\cos\theta}\times100\% $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\eta$ | 效率 | % |
| $P_{Cu}$ | 銅損（$I^2R_{eq}$） | W |
| $P_{core}$ | 鐵損 | W |

- 效率公式同樣適用於電動機與發電機〔講義 p.36〕

**例題結論**
- 例 2-5：15 kVA、2300/230 V 變壓器，滿載 0.8 落後功因時銅損 189 W、鐵損 52.5 W、輸出 12,000 W，效率 98.03%〔講義 p.37、p.42〕

**發電機的電壓調整率**〔講義 Ch.3 p.33〕
- 同樣的定義也用來比較發電機：$\text{VR} = (V_{nl} - V_{fl})/V_{fl}\times100\%$，$V_{nl}$、$V_{fl}$ 為發電機無載、滿載端電壓
- VR 為正代表電壓－電流特性**下垂**，為負代表**上升**；VR 越小，端電壓隨負載變化越穩定
- 電動機對應的指標是[速度調整率](speed-regulation.md)
- 同步發電機在不同功因下的 VR 見[發電機單獨運轉](generator-operating-alone.md)（Ch.4）

## 和其他概念的關係
- 用的是[變壓器等效電路](transformer-equivalent-circuit.md)
- 功因的定義見[交流功率](ac-power.md)；鐵損見[鐵損](core-losses.md)
- 也可以用[標么值](per-unit-system.md)表示
- 為了補償電壓變化，可以調[分接頭](transformer-taps.md)

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 p.34–42〕
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 Ch.3 p.33〕
