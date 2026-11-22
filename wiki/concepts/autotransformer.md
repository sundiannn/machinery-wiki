---
title: 自耦變壓器
en: Autotransformer
aliases: [自耦變壓器, autotransformer, 共同繞組, 串聯繞組, common winding, series winding]
chapters: [ch02]
sources: [sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 自耦變壓器（Autotransformer）

## 一句話說明
把變壓器的兩個繞組直接串起來用，只想小幅升壓或降壓時，可以用小小的變壓器處理大得多的功率；代價是失去電氣隔離。

## 白話解釋
只想把 110 V 提高到 120 V，其實只需要「多加 10 V」。自耦變壓器讓大部分功率直接通過導線，繞組只負責那「多出來的一點」，所以同一顆變壓器能處理的功率大很多〔講義 p.43、p.47〕〔AI 補充〕。

## 正式內容
**用途**：只需小幅改變電壓時（如 110→120 V、13.2→13.8 kV），用兩個完整繞組的變壓器既浪費又昂貴，改用自耦變壓器〔講義 p.43〕。

**構造與名稱**〔講義 p.43–44〕
- **共同繞組（common winding）**：電壓同時出現在兩側，匝數 $N_C$
- **串聯繞組（series winding）**：和共同繞組串聯的較小繞組，匝數 $N_{SE}$
- 低壓側為 $\mathbf{V}_L, \mathbf{I}_L$，高壓側為 $\mathbf{V}_H, \mathbf{I}_H$

**電壓與電流關係**〔講義 p.45–46〕

$$ \mathbf{V}_L = \mathbf{V}_C, \quad \mathbf{V}_H = \mathbf{V}_C + \mathbf{V}_{SE}, \quad \mathbf{I}_L = \mathbf{I}_C + \mathbf{I}_{SE}, \quad \mathbf{I}_H = \mathbf{I}_{SE} $$

$$ \frac{\mathbf{V}_L}{\mathbf{V}_H} = \frac{N_C}{N_{SE}+N_C}, \qquad \frac{\mathbf{I}_L}{\mathbf{I}_H} = \frac{N_{SE}+N_C}{N_C} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $N_C, N_{SE}$ | 共同繞組、串聯繞組匝數 | turns |
| $\mathbf{V}_C, \mathbf{V}_{SE}$ | 共同、串聯繞組電壓 | V |
| $\mathbf{I}_C, \mathbf{I}_{SE}$ | 共同、串聯繞組電流 | A |

**容量優勢**〔講義 p.46–47〕

$$ \frac{S_{IO}}{S_W} = \frac{N_{SE}+N_C}{N_{SE}} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $S_{IO}$ | 輸入（＝輸出）視在功率 | VA |
| $S_W$ | 實際通過繞組的視在功率 | VA |

**缺點**：一次與二次電路直接相連，**失去電氣隔離**；若應用不需要隔離，它是連接相近電壓的方便又便宜的選擇〔講義 p.49〕。

**例題結論**
- 例 2-7：100 VA、120/12 V 變壓器接成升壓自耦變壓器，輸出 132 V，額定容量變成 1100 VA，是原本的 11 倍〔講義 p.48–49〕

## 和其他概念的關係
- 由一般的[理想變壓器](ideal-transformer.md)改接而成
- 屬於[變壓器](transformer.md)一章

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 p.43–49〕
