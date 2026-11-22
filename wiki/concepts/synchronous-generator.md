---
title: 同步發電機
en: Synchronous Generator
aliases: [同步發電機, 交流發電機, alternator, synchronous generator, 原動機, 場繞組, 電樞繞組, prime mover]
chapters: [ch04]
sources: [sources/ch04.md]
updated: 2026-11-23
status: draft
---

# 同步發電機（Synchronous Generator）

## 一句話說明
轉子是一塊「電磁鐵」，由引擎或渦輪帶著轉，它的旋轉磁場掃過定子，就在定子產生三相交流電；轉速和電頻率完全鎖在一起，所以叫「同步」。

## 白話解釋
發電廠裡，蒸汽或水推動渦輪，渦輪帶著轉子轉；轉子上通了直流電變成電磁鐵，轉起來就是一個「旋轉磁場」。定子上的三組線圈被它掃過，就像 Ch.3 的例 3-2 一樣，產生三相電壓〔講義 p.1〕〔AI 補充〕。

## 正式內容
**構造**〔講義 p.1〕
- 轉子磁場由**永久磁鐵**或在轉子繞組通**直流電流**形成的電磁鐵產生
- 轉子由**原動機（prime mover）**帶動旋轉，在電機內形成旋轉磁場，於定子繞組感應三相電壓
- **場繞組（field windings）**：產生主磁場的繞組；**電樞繞組（armature windings）**：感應出主要電壓的繞組
- 同步電機的場繞組在轉子上，所以「轉子繞組＝場繞組」、「定子繞組＝電樞繞組」可互換使用

**轉速**〔講義 p.1–2〕
- 「同步」的意思：產生的電頻率與轉子的機械轉速**鎖定（同步）**

$$ f_{se} = \frac{n_{sm}P}{120} \quad\Longleftrightarrow\quad n_{sm} = \frac{120 f_{se}}{P} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $f_{se}$ | 電頻率 | Hz |
| $n_{sm}$ | 磁場機械轉速（＝同步電機的轉子轉速） | r/min |
| $P$ | 極數 | — |

**原動機的要求**〔講義 p.10〕
- 原動機可以是柴油引擎、蒸汽渦輪、水輪機等；不論哪一種，轉速都必須**幾乎不隨負載改變**，否則電力系統的頻率會飄移

## 本章地圖
1. 電壓從哪來：[內生電壓](internal-generated-voltage.md)
2. 模型：[同步機等效電路](synchronous-equivalent-circuit.md)（含電樞反應、同步電抗、相量圖）
3. 能送多少電：[同步機的功率與轉矩](synchronous-power-and-torque.md)
4. 參數怎麼量：[同步機參數測試](synchronous-machine-tests.md)
5. 負載變化時：[發電機單獨運轉](generator-operating-alone.md)

## 和其他概念的關係
- 屬於[交流電機](ac-machines.md)中的同步電機；運作原理是[磁場四大原理](four-magnetic-principles.md)的「發電機作用」
- 轉速公式見[電頻率與轉速](electrical-frequency-and-speed.md)
- 同一台機器反過來用就是[同步電動機](synchronous-motor.md)（Ch.5）

## 出處
- [Ch.4 來源摘要](../sources/ch04.md)〔講義 p.1–2、p.10〕
