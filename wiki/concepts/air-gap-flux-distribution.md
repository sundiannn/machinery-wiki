---
title: 氣隙磁通分布
en: MMF and Flux Distribution
aliases: [氣隙磁通分布, 分布繞組, 分數節距繞組, 磁動勢分布, distributed winding, fractional-pitch winding]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 氣隙磁通分布（MMF and Flux Distribution）

## 一句話說明
要產生漂亮的正弦波電壓，氣隙中的磁通密度沿著圓周必須呈正弦分布，做法是把繞組「分散」放在許多槽中。

## 白話解釋
想要畫出一條平滑的正弦波，卻只能用一格一格的方塊堆：方塊越多、越細，堆出來的形狀就越接近正弦波。把繞組分散放進很多槽裡，就是在做這件事〔比喻〕〔AI 補充〕。

## 正式內容
- 要在電機中產生正弦電壓，磁通密度 $B$ 的大小必須沿氣隙表面**正弦變化**；而 $B$ 只有在磁場強度 $H$（磁動勢）也正弦變化時才會如此〔講義 p.17–18〕
- 最直接的方法：把繞組分散放在電機表面許多密集的槽中，並讓每個槽的導體數依正弦規律變化〔講義 p.18–19〕
- 實際上槽數有限、每槽導體只能是整數，所以磁動勢只是**近似**正弦，會含有高次諧波〔講義 p.19〕
- 用**分數節距繞組（fractional-pitch winding）**來抑制不想要的諧波（細節見課本附錄 B.1，不在講義範圍）〔講義 p.19〕
- 設計上也常讓每槽導體數相同，而不嚴格依正弦分配〔講義 p.19〕

## 和其他概念的關係
- 正弦分布的磁通是推導[交流電機的感應電壓](ac-induced-voltage.md)的前提
- 磁動勢與磁場強度的定義見[磁路](magnetic-circuit.md)與[磁場強度與導磁係數](magnetic-field-and-permeability.md)
- 屬於[交流電機](ac-machines.md)一章

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.17–19〕
