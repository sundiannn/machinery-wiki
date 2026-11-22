---
title: 運動導體的感應電壓
en: Induced Voltage on a Moving Conductor
aliases: [運動導體的感應電壓, 動生電壓, 發電機作用, generator action]
chapters: [ch01]
sources: [sources/ch01.md]
updated: 2026-11-23
status: draft
---

# 運動導體的感應電壓（發電機作用）

## 一句話說明
導線在磁場中移動，導線兩端就會產生電壓——這就是發電機能發電的原因。

## 白話解釋
導線「切過」磁場時，裡面的電荷被推向一端，兩端就有了電壓。移動得越快、磁場越強、導線越長，電壓越大〔AI 補充〕。

## 正式內容
〔講義 p.29〕

$$ e_{ind} = (\mathbf{v}\times\mathbf{B})\cdot\mathbf{l} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $e_{ind}$ | 導線上的感應電壓 | V |
| $\mathbf{v}$ | 導線速度 | m/s |
| $\mathbf{B}$ | 磁通密度 | T |
| $\mathbf{l}$ | 在磁場中的導線長度 | m |

- $\mathbf{l}$ 沿著導線，指向與 $\mathbf{v}\times\mathbf{B}$ 夾角最小的那一端〔講義 p.29〕
- 電壓的**正端**在 $\mathbf{v}\times\mathbf{B}$ 指向的那一端〔講義 p.29〕
- 導線是斜的時候，只有沿 $\mathbf{v}\times\mathbf{B}$ 方向的分量有貢獻（要乘上夾角的 cos）〔講義 p.31〕

**例題結論**
- 例 1-8：導線以 5.0 m/s 向右移動、$B$ = 0.5 T 指入紙面、長 1.0 m，感應電壓 2.5 V，上端為正〔講義 p.30〕
- 例 1-9：導線以 10 m/s 移動、$B$ = 0.5 T、導線傾斜，感應電壓 4.33 V，下端為正〔講義 p.31〕

## 和其他概念的關係
- 這是[磁場四大原理](four-magnetic-principles.md)的第 4 個，也是**發電機作用**的基礎
- 和[法拉第定律](faraday-law.md)一樣都在產生感應電壓，但這裡的原因是「導線在動」
- 和[載流導線受力](induced-force.md)同時出現在[線性直流機](linear-dc-machine.md)中
- 線圈在磁場中旋轉時就產生正弦電壓，見[旋轉線圈](rotating-loop.md)（Ch.3）

## 出處
- [Ch.1 來源摘要](../sources/ch01.md)〔講義 p.29–31〕
