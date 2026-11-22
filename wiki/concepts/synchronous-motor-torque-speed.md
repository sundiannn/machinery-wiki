---
title: 同步電動機的轉矩與負載
en: Synchronous Motor Torque-Speed Characteristic and Load Changes
aliases: [同步電動機的轉矩與負載, 轉矩轉速特性, 脫出轉矩, 滑動極, pullout torque, slipping poles]
chapters: [ch05]
sources: [sources/ch05.md]
updated: 2026-11-23
status: draft
---

# 同步電動機的轉矩與負載

## 一句話說明
同步電動機不管負載多重，轉速都固定不變；但負載超過**脫出轉矩**，轉子就會「掉隊」失去同步。

## 白話解釋
負載變重時，轉子只是稍微「往後退」一點（轉矩角變大）來產生更大的轉矩，速度不變。可是如果負載重到轉矩角超過 90°，磁場再也拉不住轉子，整台電機會劇烈震動〔講義 p.6–8〕〔AI 補充〕。

## 正式內容
**轉矩－轉速特性**〔講義 p.6–7〕
- 轉速鎖定在磁場轉速，而磁場轉速鎖定在電源頻率，所以**轉速與負載無關**：$n_m = 120f_{se}/P$
- 從無載到最大轉矩，穩態轉速都固定 → **速度調整率 0%**
- 轉矩式 $\tau_{ind} = kB_RB_{net}\sin\delta = \dfrac{3V_\phi E_A\sin\delta}{\omega_mX_S}$

**脫出轉矩（pullout torque）**〔講義 p.7–8〕

$$ \tau_{max} = kB_RB_{net} = \frac{3V_\phi E_A}{\omega_mX_S}\quad(\delta = 90°) $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\tau_{max}$ | 脫出轉矩（最大轉矩） | N·m |
| $V_\phi$ | 每相電壓 | V |
| $E_A$ | 內生電壓 | V |
| $\omega_m$ | 機械角速度 | rad/s |
| $X_S$ | 同步電抗 | Ω |

- 脫出轉矩通常約為滿載轉矩的 3 倍〔講義 p.6〕
- 超過脫出轉矩時，轉子無法再鎖住，開始落後；定子磁場一圈圈「超車」，轉子轉矩方向不斷反轉，巨大的轉矩突波使整台電機劇烈震動——這種失步稱為**滑動極（slipping poles）**〔講義 p.7〕
- 場電流（$E_A$）越大，最大轉矩越大 → 以大場電流運轉有**穩定性**上的好處〔講義 p.7–8〕

**負載變化時的相量圖**〔講義 p.8–9〕
- 加負載 → 轉子先減速 → 轉矩角 $\delta$ 變大 → 感應轉矩增加 → 轉子回到同步轉速，但 $\delta$ 較大
- 轉速由電源固定、場電流沒動，所以 $|\mathbf{E}_A| = K\phi\omega$ **大小不變**
- 與功率成正比的 $E_A\sin\delta$、$I_A\cos\theta$ 變大，$\mathbf{E}_A$ 沿著固定半徑的圓「往下擺」
- $jX_S\mathbf{I}_A$ 要從 $\mathbf{E}_A$ 尖端連到 $\mathbf{V}_\phi$，所以電樞電流增加；功因角也跟著改變，由超前漸漸變得較不超前、再變成落後

## 和其他概念的關係
- 轉矩式見[同步機的功率與轉矩](synchronous-power-and-torque.md)；SR 的定義見[速度調整率](speed-regulation.md)
- 轉速公式見[電頻率與轉速](electrical-frequency-and-speed.md)
- 屬於[同步電動機](synchronous-motor.md)一章

## 出處
- [Ch.5 來源摘要](../sources/ch05.md)〔講義 p.6–9〕
