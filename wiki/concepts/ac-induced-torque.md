---
title: 交流電機的感應轉矩
en: Induced Torque in AC Machines
aliases: [交流電機的感應轉矩, 感應轉矩, 轉矩角, induced torque]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 交流電機的感應轉矩（Induced Torque in AC Machines）

## 一句話說明
交流電機的轉矩來自**轉子磁場和定子磁場互相拉扯**，就像兩塊磁鐵靠近時會轉向對齊。

## 白話解釋
轉子磁場想和淨磁場對齊。如果轉子磁場「領先」，轉矩就把它往回拉（發電機在抵抗推力）；如果轉子磁場「落後」，轉矩就把它往前拉（電動機被帶著轉）〔講義 p.26、p.30〕〔AI 補充〕。

## 正式內容
- 正常運轉時，交流電機內有轉子電路與定子電路兩個磁場，兩者的交互作用產生轉矩，就像兩塊靠近的永久磁鐵會轉向對齊〔講義 p.26〕

$$ \tau_{ind} = k\,\mathbf{B}_R\times\mathbf{B}_S = k\,\mathbf{B}_R\times\mathbf{B}_{net}, \qquad \tau_{ind} = kB_RB_{net}\sin\delta $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\mathbf{B}_R$ | 轉子磁通密度 | T |
| $\mathbf{B}_S$ | 定子磁通密度 | T |
| $\mathbf{B}_{net}$ | 淨磁通密度（$= \mathbf{B}_R + \mathbf{B}_S$，不考慮飽和） | T |
| $\delta$ | $\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ 的夾角 | ° |
| $k$ | 和構造有關的常數 | — |

〔講義 p.28–30〕

- $k$ 一般**不是常數**，因為導磁係數會隨飽和程度改變；此式主要用來做**定性**分析〔講義 p.29〕
- 此式和單一[旋轉線圈](rotating-loop.md)的轉矩式相同，適用於任何交流電機，只有 $k$ 不同〔講義 p.29〕
- 因為向量和自己的外積為零，$\mathbf{B}_R\times\mathbf{B}_S$ 可改寫成 $\mathbf{B}_R\times\mathbf{B}_{net}$〔講義 p.29〕

**判斷發電機或電動機**〔講義 p.30〕
- 用右手定則判斷感應轉矩方向：若感應轉矩方向與轉子旋轉方向**相反**，這台電機在當**發電機**（講義 Figure 3-19 的例子）

## 和其他概念的關係
- 兩個磁場之一是[旋轉磁場](rotating-magnetic-field.md)
- 轉換的功率 $P_{conv} = \tau_{ind}\omega_m$，見[電機損失與功率流](machine-losses-and-power-flow.md)
- 在同步機中，$\delta$ 決定功率與轉矩，見[同步機的功率與轉矩](synchronous-power-and-torque.md)（Ch.4）
- 屬於[交流電機](ac-machines.md)一章

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.26–30〕
