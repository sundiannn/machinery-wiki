---
title: 實際變壓器
en: Real Single-Phase Transformer
aliases: [實際變壓器, 互磁通, 漏磁通, 激磁電流, 磁化電流, 鐵損電流, mutual flux, leakage flux, excitation current]
chapters: [ch02]
sources: [sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 實際變壓器（Real Single-Phase Transformer）

## 一句話說明
真實的變壓器有一點磁通會「漏掉」，而且即使不接負載，也需要一小股電流來建立磁通和補鐵損。

## 白話解釋
理想變壓器像完全不漏水的水管；實際的變壓器會漏一點水（漏磁通），而且要先花一點水把管子灌滿（激磁電流）。好的變壓器漏得很少、灌滿所需的水也很少〔比喻〕〔AI 補充〕。

## 正式內容
**電壓比從法拉第定律來**〔講義 p.13–15〕
- 定義每匝平均磁通 $\bar\phi = \lambda/N$，忽略繞組電阻時 $\bar\phi = \dfrac{1}{N_P}\displaystyle\int v_P(t)\,dt$：鐵心磁通正比於外加電壓的積分
- 一次線圈的磁通分成兩部分：留在鐵心、同時穿過兩個繞組的**互磁通** $\phi_M$，和經空氣繞回、只穿過自己繞組的**漏磁通** $\phi_{LP}$（二次側同理）
- 互磁通產生的電壓比恰好等於匝數比：$e_P/e_S = N_P/N_S = a$
- 設計良好的變壓器 $\phi_M \gg \phi_{LP}$、$\phi_M \gg \phi_{LS}$，所以 $v_P/v_S \approx a$

**激磁電流（excitation current）**：二次側開路時一次側仍有電流，由兩部分組成〔講義 p.16–18〕

| 成分 | 作用 | 特性 |
|---|---|---|
| 磁化電流 $i_M$ | 在鐵心中建立磁通 | 基本波落後電壓 90°；鐵心飽和使它不是正弦波、含高頻諧波 |
| 鐵損電流 $i_{h+e}$ | 補充磁滯損與渦流損 | 基本波與電壓同相；磁通經過零時最大 |

- 鐵心磁通峰值一到飽和點，磁通再增加一點點，磁化電流峰值就會大增；越飽和，諧波越大〔講義 p.16〕
- 設計良好的電力變壓器，激磁電流遠小於滿載電流〔講義 p.18〕

**電流比**〔講義 p.18–20〕
- 接負載時，鐵心的淨磁動勢 $N_P i_P - N_S i_S = \phi\,\mathfrak{R}$
- 設計良好的鐵心在未飽和時磁阻幾乎為零，所以 $N_P i_P \approx N_S i_S$，即 $i_P/i_S \approx 1/a$

## 和其他概念的關係
- 從[理想變壓器](ideal-transformer.md)出發，加上本頁的非理想效應
- 這些效應整理成電路就是[變壓器等效電路](transformer-equivalent-circuit.md)
- 漏磁通的來源見[磁場強度與導磁係數](magnetic-field-and-permeability.md)；磁交鏈見[法拉第定律](faraday-law.md)
- 磁化電流不是正弦波的原因見[磁化曲線](magnetization-curve.md)；鐵損電流對應[鐵損](core-losses.md)

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 p.12–20〕
