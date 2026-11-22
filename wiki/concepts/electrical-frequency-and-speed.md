---
title: 電頻率與轉速
en: Electrical Frequency and Speed of Rotation
aliases: [電頻率與轉速, 極數, 同步轉速, 電機角, 機械角, poles, synchronous speed]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 電頻率與轉速（Electrical Frequency and Speed of Rotation）

## 一句話說明
磁極越多，磁場轉得越慢：60 Hz 的電，兩極電機每分鐘轉 3600 圈，四極電機只轉 1800 圈。

## 白話解釋
兩極電機的電流變化一個週期，磁場剛好轉一圈；四極電機一個週期只轉半圈，因為同樣的「N-S」花紋在一圈中重複了兩次〔講義 p.13–15〕〔AI 補充〕。

## 正式內容
- **兩極定子**：每一個電氣週期，磁極在定子表面剛好轉一圈機械圈，所以機械轉速（rps）等於電頻率（Hz）〔講義 p.13〕
- **四極定子**：一個電氣週期 360° 電機角，只對應 180° 機械角，所以電頻率是機械轉速的兩倍〔講義 p.14〕
- **一般 $P$ 極**：繞組順序 a-c'-b-a'-c-b' 在定子內表面重複 $P/2$ 次〔講義 p.15〕

$$ \theta_{se} = \frac{P}{2}\theta_{sm}, \qquad f_{se} = \frac{P}{2}f_{sm}, \qquad \omega_{se} = \frac{P}{2}\omega_{sm}, \qquad f_{se} = \frac{n_{sm}P}{120} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P$ | 磁極數 | — |
| $\theta_{se}, \theta_{sm}$ | 定子的電機角、機械角 | ° |
| $f_{se}$ | 定子電流的電頻率 | Hz |
| $f_{sm}$ | 定子磁場的機械轉速 | rps |
| $\omega_{se}, \omega_{sm}$ | 電角速度、機械角速度 | rad/s |
| $n_{sm}$ | 定子磁場的機械轉速 | rpm |

〔講義 p.15–16〕

## 和其他概念的關係
- 描述的是[旋轉磁場](rotating-magnetic-field.md)的轉速
- 機械轉速的單位換算見[旋轉運動](rotational-motion.md)
- 同步電機的轉子轉速就等於磁場轉速，見[同步發電機](synchronous-generator.md)（Ch.4）
- 屬於[交流電機](ac-machines.md)一章

## 常見誤解
- 公式中的 $P$ 是「極數」不是「極對數」：四極電機 $P = 4$〔講義 p.15〕

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.13–16〕
