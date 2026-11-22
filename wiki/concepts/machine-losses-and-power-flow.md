---
title: 電機損失與功率流
en: AC Machine Power Flows and Losses
aliases: [電機損失與功率流, 功率流程圖, 銅損, 機械損, 雜散損, 無載旋轉損, power-flow diagram, copper loss, stray loss]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 電機損失與功率流（AC Machine Power Flows and Losses）

## 一句話說明
電機在轉換能量的路上會一路「漏掉」一些功率；功率流程圖把輸入、各種損失、轉換點、輸出畫成一條河流，一目了然。

## 白話解釋
像一條河從上游流到下游，沿途被幾條小溝渠分走一些水：發電機的上游是機械功率，先被摩擦、鐵損等分掉，剩下的在「轉換點」變成電，再被線圈的電阻分走一點，才到達出口〔比喻〕〔AI 補充〕。

## 正式內容
**效率**〔講義 p.30–31〕

$$ \eta = \frac{P_{out}}{P_{in}}\times100\% = \frac{P_{in} - P_{loss}}{P_{in}}\times100\% $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P_{in}, P_{out}$ | 輸入、輸出功率 | W |
| $P_{loss}$ | 電機內部的總損失 | W |

**四類損失**〔講義 p.31–32〕

| 類別 | 內容 |
|---|---|
| 電氣損失（銅損） | 定子（電樞）與轉子（場）繞組的 $I^2R$ 發熱 |
| 鐵損 | 鐵心金屬中的磁滯損與渦流損 |
| 機械損失 | 摩擦（friction）與風阻（windage） |
| 雜散損失 | 無法歸入前三類的損失，慣例上取滿載的 1% |

$$ P_{SCL} = 3I_A^2R_A, \qquad P_{RCL} = I_F^2R_F $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P_{SCL}$ | 定子銅損（三相） | W |
| $I_A, R_A$ | 每相電樞（定子）電流、電阻 | A、Ω |
| $P_{RCL}$ | 轉子銅損（同步電機） | W |
| $I_F, R_F$ | 轉子場繞組電流、電阻 | A、Ω |

- 計算用的電阻通常取正常運轉溫度下的繞組電阻〔講義 p.31〕
- 機械損失與鐵損常合稱**無載旋轉損（no-load rotational loss）**〔講義 p.31〕

**功率流程圖**〔講義 p.32〕

$$ P_{conv} = \tau_{ind}\,\omega_m $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P_{conv}$ | 從機械形式轉換成電氣形式（或反過來）的功率 | W |
| $\tau_{ind}$ | 感應轉矩 | N·m |
| $\omega_m$ | 機械角速度 | rad/s |

- **發電機**：輸入機械功率 $P_{in} = \tau_{app}\omega_m$ → 扣掉雜散損、機械損、鐵損 → 在 $P_{conv}$ 轉成電 → 扣掉 $I^2R$ 損失 → 輸出 $P_{out} = 3V_\phi I_A\cos\theta = \sqrt3V_LI_L\cos\theta$〔講義 p.32〕
- **電動機**：流程反過來，輸入 $P_{in} = 3V_\phi I_A\cos\theta$ → 扣掉 $I^2R$ 損失 → 在 $P_{conv}$ 轉成機械 → 扣掉鐵損、機械損、雜散損 → 輸出 $P_{out} = \tau_{load}\omega_m$〔講義 p.32〕

## 和其他概念的關係
- 鐵損的成因見[鐵損](core-losses.md)
- $P = \tau\omega$ 見[旋轉運動](rotational-motion.md)；轉矩見[交流電機的感應轉矩](ac-induced-torque.md)
- 效率的定義與變壓器相同，見[電壓調整率與效率](voltage-regulation-and-efficiency.md)
- 屬於[交流電機](ac-machines.md)一章

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.30–32〕
