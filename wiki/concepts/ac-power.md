---
title: 交流功率
en: AC Power
aliases: [交流功率, 實功率, 虛功率, 視在功率, 功率因數, real power, reactive power, apparent power, power factor]
chapters: [ch02, ch05]
sources: [sources/ch02.md, sources/ch05.md]
updated: 2026-11-23
status: draft
---

# 交流功率（實功率、虛功率、視在功率）

## 一句話說明
交流電路中，電壓和電流不一定同步；真正做功的是**實功率** $P$，來回交換的是**虛功率** $Q$，兩者合起來的「總量」是**視在功率** $S$。

## 白話解釋
像一杯啤酒：下面的酒是實功率（真正喝得到），上面的泡沫是虛功率（占空間但沒喝到），整杯的量是視在功率〔比喻〕〔AI 補充〕。

## 正式內容
本頁只整理 Ch.2 講義中用到的式子（Ch.1 講義缺 1.9 節，見 [Ch.1 來源摘要](../sources/ch01.md)）〔講義 Ch.2 p.5–6〕：

$$ P = VI\cos\theta, \qquad Q = VI\sin\theta, \qquad S = VI $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P$ | 實功率（real power） | W |
| $Q$ | 虛功率（reactive power） | var |
| $S$ | 視在功率（apparent power） | VA |
| $V, I$ | 電壓、電流的有效值 | V、A |
| $\theta$ | 電壓與電流之間的夾角（功率因數角） | ° |

- $\cos\theta$ 稱為**功率因數（power factor, PF）**〔講義 Ch.2 p.6〕
- 電流落後電壓叫**落後（lagging）**功因，電流超前電壓叫**超前（leading）**功因〔講義 Ch.2 p.25、p.35〕
- 變壓器、電機的容量常用視在功率（kVA）標示，例如「20 kVA 變壓器」〔講義 Ch.2 p.27〕

**由 $P$ 與功因求 $Q$**〔講義 Ch.5 p.20〕

$$ Q = S\sin\theta = \frac{P}{\cos\theta}\sin\theta = P\tan\theta $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\theta$ | 功率因數角（落後為正、超前為負） | ° |

## 和其他概念的關係
- 理想變壓器的 $P$、$Q$、$S$ 都輸入等於輸出，見[理想變壓器](ideal-transformer.md)
- 功因會影響變壓器的電壓調整率，見[電壓調整率與效率](voltage-regulation-and-efficiency.md)
- 提高系統功因可以降低輸電損失，見[功率因數校正](power-factor-correction.md)（Ch.5）

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 Ch.2 p.5–6〕
- [Ch.5 來源摘要](../sources/ch05.md)〔講義 Ch.5 p.20〕
