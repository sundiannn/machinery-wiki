---
title: 法拉第定律
en: Faraday's Law
aliases: [法拉第定律, 冷次定律, 楞次定律, 磁交鏈, 感應電壓, Lenz's law, flux linkage]
chapters: [ch01, ch02]
sources: [sources/ch01.md, sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 法拉第定律（Faraday's Law）

## 一句話說明
穿過線圈的磁通**一變化**，線圈就會感應出電壓；變化越快，電壓越大。

## 白話解釋
重點在「變化」：磁通再大，只要不變，就不會感應出電壓。線圈還有點「固執」，感應出的電壓方向總是想抵抗磁通的變化（冷次定律）〔AI 補充〕。

## 正式內容
**單匝與 N 匝線圈**〔講義 p.24〕

$$ e_{ind} = -\frac{d\phi}{dt}, \qquad e_{ind} = -N\frac{d\phi}{dt} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $e_{ind}$ | 感應電壓 | V |
| $N$ | 線圈匝數 | turns |
| $\phi$ | 穿過線圈的磁通 | Wb |
| $t$ | 時間 | s |

**冷次定律（Lenz's law）**：式中的負號代表感應電壓的方向，會使（若線圈兩端短路時）產生的電流所建立的磁通**反抗**原本磁通的變化〔講義 p.24–25〕。

**磁交鏈（flux linkage）**〔講義 p.25–26〕
- 上式假設每一匝的磁通都相同，但漏磁通使這個假設不成立
- 改用每一匝各自的磁通 $\phi_i$ 加總：

$$ \lambda = \sum_{i=1}^{N}\phi_i, \qquad e_{ind} = \frac{d\lambda}{dt} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\lambda$ | 磁交鏈 | Wb·turns |
| $\phi_i$ | 穿過第 $i$ 匝的磁通 | Wb |

**例題結論**
- 例 1-6：100 匝線圈、磁通 $\phi = 0.05\sin377t$ Wb，感應電壓 $e_{ind} = 1885\sin(377t+90°)$ V；極性由冷次定律判斷〔講義 p.27〕

**在變壓器中的應用**〔講義 Ch.2 p.13〕
- 定義每匝平均磁通 $\bar\phi = \lambda/N$，法拉第定律可寫成 $e_{ind} = N\,d\bar\phi/dt$；外加電壓決定鐵心磁通

## 和其他概念的關係
- 這是[磁場四大原理](four-magnetic-principles.md)的第 2 個，也是**變壓器作用**的基礎
- 渦流也是法拉第定律造成的，見[鐵損](core-losses.md)
- 漏磁通的來源見[磁場強度與導磁係數](magnetic-field-and-permeability.md)
- 導體在磁場中運動的情況見[運動導體的感應電壓](motional-voltage.md)

- 變壓器的電壓比直接由法拉第定律推出：互磁通在兩個繞組感應的電壓比等於匝數比，見[實際變壓器](real-transformer.md)

## 出處
- [Ch.1 來源摘要](../sources/ch01.md)〔講義 p.24–27〕
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 Ch.2 p.13–15〕
