---
title: 磁路
en: Magnetic Circuit
aliases: [磁路, 磁動勢, 磁阻, 磁導, 邊緣效應, 氣隙, mmf, reluctance, fringing]
chapters: [ch01]
sources: [sources/ch01.md]
updated: 2026-11-23
status: draft
---

# 磁路（Magnetic Circuit）

## 一句話說明
把磁通在鐵心中的路徑當成「電路」來分析：磁動勢推動磁通，磁阻阻礙磁通。

## 白話解釋
就像水管：水泵（磁動勢）推水（磁通）流過水管，細長的水管阻力大（磁阻大）。鐵心是很粗的水管，空氣氣隙則像一段很細的管子，即使很短也會擋住大部分水流〔比喻〕〔AI 補充〕。

## 正式內容
**電路與磁路的對照**〔講義 p.8–10〕

| 電路 | 磁路 |
|---|---|
| 電壓（電動勢）$V$ | 磁動勢 $\mathfrak{F} = Ni$ |
| 電流 $I$ | 磁通 $\phi$ |
| 電阻 $R$ | 磁阻 $\mathfrak{R}$ |
| 電導 $G = 1/R$ | 磁導 $\mathcal{P} = 1/\mathfrak{R}$ |
| 歐姆定律 $V = IR$ | $\mathfrak{F} = \phi\mathfrak{R}$ |

$$ \mathfrak{F} = Ni, \qquad \mathfrak{F} = \phi\,\mathfrak{R}, \qquad \mathfrak{R} = \frac{l_c}{\mu A} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\mathfrak{F}$ | 磁動勢（magnetomotive force, mmf） | A·turns |
| $\phi$ | 磁通 | Wb |
| $\mathfrak{R}$ | 磁阻（reluctance） | A·turns/Wb |
| $\mathcal{P}$ | 磁導（permeance） | Wb/(A·turns) |
| $l_c$ | 平均路徑長 | m |
| $\mu$ | 導磁係數 | H/m |
| $A$ | 截面積 | m² |

- **磁動勢的極性**：右手四指沿線圈電流方向彎曲，拇指指向正的磁動勢方向〔講義 p.9〕
- **串聯**：$\mathfrak{R}_{eq} = \mathfrak{R}_1 + \mathfrak{R}_2 + \cdots$；**並聯**：$\dfrac{1}{\mathfrak{R}_{eq}} = \dfrac{1}{\mathfrak{R}_1} + \dfrac{1}{\mathfrak{R}_2} + \cdots$〔講義 p.10〕

**磁路計算只是近似**，最好也只有約 5% 的誤差，原因有四〔講義 p.10–11〕：
1. 漏磁通
2. 平均路徑長與截面積在轉角處並不準確
3. 鐵磁材料的導磁係數會變化
4. **邊緣效應（fringing effect）**：磁通在氣隙會向外擴散，使氣隙的有效截面積比鐵心大

**例題結論**
- 鐵心各段截面積不同時，分段算磁阻再串聯（例 1-1，磁通 0.0048 Wb）〔講義 p.12–13〕
- 氣隙比鐵心短 800 倍，卻貢獻大部分磁阻（例 1-2）→ [例題引導](../examples/ch01-air-gap.md)〔講義 p.14–15〕
- 直流電動機的轉子、定子與兩個氣隙串聯，算出氣隙磁通密度 0.19 T（例 1-3）〔講義 p.16–17〕

## 和其他概念的關係
- 公式來自[磁場強度與導磁係數](magnetic-field-and-permeability.md)
- 鐵心飽和時磁阻會改變，見[磁化曲線](magnetization-curve.md)

## 常見誤解
- 求**氣隙**的磁通密度時，要用含邊緣效應的**氣隙有效面積**，不是鐵心面積〔講義 p.15〕

## 出處
- [Ch.1 來源摘要](../sources/ch01.md)〔講義 p.8–17〕
