---
title: 同步機的功率與轉矩
en: Power and Torque in Synchronous Machines
aliases: [同步機的功率與轉矩, 功率角曲線, 靜態穩定限度, 轉矩角, static stability limit]
chapters: [ch04]
sources: [sources/ch04.md]
updated: 2026-11-23
status: draft
---

# 同步機的功率與轉矩（Power and Torque in Synchronous Machines）

## 一句話說明
同步發電機送出的功率由**轉矩角 $\delta$** 決定：$P = 3V_\phi E_A\sin\delta / X_S$，$\delta = 90°$ 時最大。

## 白話解釋
轉子磁場和淨磁場之間像有一條彈簧：原動機推得越用力，彈簧被拉開的角度 $\delta$ 越大，送出的電功率就越多。但拉到 90° 就是極限，再拉就「斷」了（失去同步）〔比喻〕〔AI 補充〕。

## 正式內容
**功率流**〔講義 p.10–11〕
- 輸入機械功率 $P_{in} = \tau_{app}\omega_m$；扣掉機械損、鐵損、雜散損後轉換：

$$ P_{conv} = \tau_{ind}\omega_m = 3E_AI_A\cos\gamma $$

$$ P_{out} = \sqrt3V_LI_L\cos\theta = 3V_\phi I_A\cos\theta, \qquad Q_{out} = \sqrt3V_LI_L\sin\theta = 3V_\phi I_A\sin\theta $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\gamma$ | $\mathbf{E}_A$ 與 $\mathbf{I}_A$ 的夾角 | ° |
| $\theta$ | $\mathbf{V}_\phi$ 與 $\mathbf{I}_A$ 的夾角（功率因數角） | ° |
| $V_L, I_L$ | 線電壓、線電流 | V、A |

**功率角公式**（忽略 $R_A$）〔講義 p.11–12〕
- 簡化相量圖中同一段可寫成 $E_A\sin\delta$ 或 $X_SI_A\cos\theta$，代入得：

$$ P = \frac{3V_\phi E_A\sin\delta}{X_S}, \qquad P_{max} = \frac{3V_\phi E_A}{X_S} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\delta$ | 內角（轉矩角），$\mathbf{V}_\phi$ 與 $\mathbf{E}_A$ 的夾角 | ° |
| $X_S$ | 同步電抗 | Ω |
| $P_{max}$ | 靜態穩定限度（$\delta = 90°$） | W |

- $P_{max}$ 稱為**靜態穩定限度（static stability limit）**；實際發電機不會接近此限，滿載轉矩角通常為 20°～30°〔講義 p.12–13〕
- 若 $V_\phi$ 固定：實功率正比於 $I_A\cos\theta$ 與 $E_A\sin\delta$，虛功率正比於 $I_A\sin\theta$〔講義 p.13〕

**轉矩**〔講義 p.13〕

$$ \tau_{ind} = kB_RB_{net}\sin\delta = \frac{3V_\phi E_A\sin\delta}{\omega_mX_S} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\omega_m$ | 機械角速度 | rad/s |

- 前式用**磁**量描述，後式用**電**量描述同一件事；轉換功率與感應轉矩都取決於轉矩角 $\delta$〔講義 p.13〕

## 和其他概念的關係
- 由[同步機等效電路](synchronous-equivalent-circuit.md)的相量圖推出
- 磁量形式見[交流電機的感應轉矩](ac-induced-torque.md)；功率流程見[電機損失與功率流](machine-losses-and-power-flow.md)
- 功率的定義見[交流功率](ac-power.md)
- 在電動機中，$\delta = 90°$ 的轉矩稱為脫出轉矩，見[同步電動機的轉矩與負載](synchronous-motor-torque-speed.md)（Ch.5）
- 屬於[同步發電機](synchronous-generator.md)一章

## 出處
- [Ch.4 來源摘要](../sources/ch04.md)〔講義 p.10–13〕
