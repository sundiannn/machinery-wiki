---
title: 旋轉線圈
en: Simple Loop in a Uniform Magnetic Field
aliases: [旋轉線圈, 均勻磁場中的旋轉線圈, 簡單旋轉線圈, simple loop]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 旋轉線圈（Simple Loop in a Uniform Magnetic Field）

## 一句話說明
一個在磁鐵中轉動的線圈，就是最簡單的交流發電機：轉一圈，就產生一個完整的正弦波電壓；通電時，它也會受到轉矩，變成電動機。

## 白話解釋
線圈轉動時，它的兩條邊輪流「切過」磁場，一下往這邊、一下往那邊，所以產生的電壓一正一負交替——這就是「交流電」的由來〔AI 補充〕。

## 正式內容
**感應電壓**〔講義 p.1–4〕
- 把線圈四段分開算：與轉軸平行的兩段（ab、cd）有電壓，另外兩段的 $\mathbf{v}\times\mathbf{B}$ 和導線垂直，電壓為零
- 以等角速度 $\omega$ 旋轉時 $\theta = \omega t$，邊緣速度 $v = r\omega$

$$ e_{ind} = 2vBl\sin\theta = 2r\omega Bl\sin\omega t = AB\omega\sin\omega t = \phi_{max}\,\omega\sin\omega t $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $r$ | 轉軸到線圈邊的半徑 | m |
| $l$ | 線圈邊長 | m |
| $A$ | 線圈面積（$= 2rl$） | m² |
| $\phi_{max}$ | 穿過線圈的最大磁通（$= AB$，線圈垂直磁場時） | Wb |
| $\omega$ | 角速度 | rad/s |

- 電壓是正弦波，大小等於機器內的磁通乘上轉速；任何真實電機的電壓都取決於三件事：**磁通、轉速、構造**（線圈數等）〔講義 p.4〕

**感應轉矩**〔講義 p.4–7〕
- 線圈通電流 $i$ 時，每段受力 $\mathbf{F} = i(\mathbf{l}\times\mathbf{B})$；只有 ab、cd 兩段產生轉矩

$$ \tau_{ind} = 2rilB\sin\theta = k\,\mathbf{B}_{loop}\times\mathbf{B}_S $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\theta$ | 線圈與磁場的夾角 | ° |
| $\mathbf{B}_{loop}$ | 線圈電流產生的磁通密度（垂直線圈平面） | T |
| $\mathbf{B}_S$ | 外部（定子）磁通密度 | T |
| $k$ | 和構造有關的常數 | — |

- 線圈平面與磁場平行時轉矩最大，垂直時轉矩為零〔講義 p.7〕
- 任何真實電機的轉矩都取決於四件事：**轉子磁場強度、外部磁場強度、兩者夾角的正弦、構造常數**〔講義 p.7–8〕

## 和其他概念的關係
- 電壓用的是[運動導體的感應電壓](motional-voltage.md)，轉矩用的是[載流導線受力](induced-force.md)
- 推廣到真實電機，見[交流電機的感應電壓](ac-induced-voltage.md)與[交流電機的感應轉矩](ac-induced-torque.md)
- 屬於[交流電機](ac-machines.md)一章；完整示範見[例 3-2](../examples/ch03-simple-generator.md)

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.1–8〕
