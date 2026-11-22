---
title: 磁場強度與導磁係數
en: Magnetic Field Intensity and Permeability
aliases: [磁場強度, 磁通密度, 導磁係數, 相對導磁係數, 安培定律, 磁通, permeability, flux density]
chapters: [ch01, ch02]
sources: [sources/ch01.md, sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 磁場強度與導磁係數（Magnetic Field Intensity and Permeability）

## 一句話說明
電流產生磁場強度 $H$，材料的導磁係數 $\mu$ 決定能產生多少磁通密度 $B$；鐵的導磁係數是空氣的幾千倍。

## 白話解釋
$H$ 是電流「多努力」在建立磁場〔講義 p.7〕；$\mu$ 是材料「多容易被磁化」。同樣的努力，用在鐵上得到的磁場比空氣多幾千倍，所以電機都用鐵心〔AI 補充〕。

## 正式內容
**安培定律（Ampere's law）**：電流產生磁場的基本定律〔講義 p.6〕

$$ \oint \mathbf{H}\cdot d\mathbf{l} = I_{net} $$

在繞了 $N$ 匝線圈的鐵心中，積分路徑取鐵心的平均路徑長 $l_c$，包圍的電流為 $Ni$〔講義 p.6–7〕：

$$ H l_c = Ni \quad\Rightarrow\quad H = \frac{Ni}{l_c} $$

**磁場強度與磁通密度**〔講義 p.7〕

$$ \mathbf{B} = \mu\mathbf{H}, \qquad \mu_0 = 4\pi\times10^{-7}\ \text{H/m}, \qquad \mu_r = \frac{\mu}{\mu_0} $$

**磁通**：穿過某個面積的磁通密度總量〔講義 p.8〕

$$ \phi = \int_A \mathbf{B}\cdot d\mathbf{A} \;\Rightarrow\; \phi = BA \quad(\mathbf{B}\text{ 垂直且均勻時}) $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $H$ | 磁場強度（magnetic field intensity） | A·turns/m |
| $I_{net}$ | 積分路徑所包圍的淨電流 | A |
| $N$ | 線圈匝數 | turns |
| $l_c$ | 鐵心平均路徑長 | m |
| $B$ | 磁通密度（magnetic flux density） | T（= Wb/m²） |
| $\mu$ | 導磁係數（permeability） | H/m |
| $\mu_0$ | 真空導磁係數 | H/m |
| $\mu_r$ | 相對導磁係數（relative permeability） | — |
| $\phi$ | 磁通（flux） | Wb |
| $A$ | 截面積 | m² |

**重要數字與觀念**
- 電機用的鋼材 $\mu_r$ 約 2000～6000 以上：同樣電流下，鋼中建立的磁通是空氣的 2000～6000 倍〔講義 p.7〕
- 因此鐵心中的磁通絕大部分都留在鐵心內；少量漏出的**漏磁通（leakage flux）**很重要，它決定了線圈間的磁交鏈與自感〔講義 p.7〕
- 鐵心中的磁通〔講義 p.8〕：$\phi = \dfrac{\mu N i A}{l_c}$

**在變壓器中**〔講義 Ch.2 p.13–14、p.20–21〕
- 只穿過一個繞組、經空氣繞回的漏磁通，在等效電路中用漏電感（漏電抗）表示，見[變壓器等效電路](transformer-equivalent-circuit.md)

## 和其他概念的關係
- 這是[磁場四大原理](four-magnetic-principles.md)的第 1 個
- 把這些式子整理成「類似電路」的形式，就是[磁路](magnetic-circuit.md)
- 鐵的 $\mu$ 不是常數，見[磁化曲線](magnetization-curve.md)
- 磁交鏈的定義見[法拉第定律](faraday-law.md)

## 出處
- [Ch.1 來源摘要](../sources/ch01.md)〔講義 p.6–8〕
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 Ch.2 p.13–14、p.20–21〕
