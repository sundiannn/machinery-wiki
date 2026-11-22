---
title: 交流電機的感應電壓
en: Induced Voltage in AC Machines
aliases: [交流電機的感應電壓, 內生電壓, 相電壓, E_A, induced voltage]
chapters: [ch03]
sources: [sources/ch03.md]
updated: 2026-11-23
status: draft
---

# 交流電機的感應電壓（Induced Voltage in AC Machines）

## 一句話說明
旋轉的轉子磁場掃過定子上三組相隔 120° 的線圈，就感應出三相電壓；每相電壓的有效值是 $E_A = \sqrt2\pi N_C\phi f$。

## 白話解釋
這是旋轉磁場「反過來用」：三相電流能產生旋轉磁場，旋轉磁場也能在三相線圈中產生三相電壓——這就是交流發電機〔講義 p.20〕〔AI 補充〕。

## 正式內容
**單一線圈**〔講義 p.20–23〕
- 假設轉子在氣隙中的磁通密度沿圓周正弦分布、方向徑向朝外
- 「坐在磁場上」看，就像磁場不動、線圈以相對速度掠過，可以直接套用 $e = (\mathbf{v}\times\mathbf{B})\cdot\mathbf{l}$
- 單匝線圈的磁通 $\phi = 2rlB_M$；兩極定子時 $\omega_m = \omega_e = \omega$，得 $e_{ind} = \phi\omega\cos\omega t$；$N_C$ 匝線圈為 $e_{ind} = N_C\phi\omega\cos\omega t$

**三相電壓**〔講義 p.23–24〕

$$ e_{aa'} = N_C\phi\omega\sin\omega t,\quad e_{bb'} = N_C\phi\omega\sin(\omega t - 120°),\quad e_{cc'} = N_C\phi\omega\sin(\omega t - 240°) $$

**峰值與有效值**〔講義 p.24〕

$$ E_{max} = N_C\phi\omega = 2\pi N_C\phi f, \qquad E_A = \frac{2\pi}{\sqrt2}N_C\phi f = \sqrt2\,\pi N_C\phi f $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $N_C$ | 每個線圈的匝數 | turns |
| $\phi$ | 每極磁通 | Wb |
| $\omega$ | 角頻率（$= 2\pi f$） | rad/s |
| $f$ | 電頻率 | Hz |
| $E_{max}$ | 每相電壓峰值 | V |
| $E_A$ | 每相電壓有效值 | V |

- 端電壓有效值：**Y 接**為 $\sqrt3E_A$，**Δ 接**等於 $E_A$〔講義 p.24〕

**例題結論**
- 例 3-2：兩極發電機，每相峰值 169.7 V、有效值 120 V，Y 接端電壓 208 V → [例題引導](../examples/ch03-simple-generator.md)〔講義 p.25–26〕

## 和其他概念的關係
- 由[旋轉線圈](rotating-loop.md)推廣而來，前提是[氣隙磁通分布](air-gap-flux-distribution.md)為正弦
- 與[旋轉磁場](rotating-magnetic-field.md)互為相反過程
- Y 與 Δ 的線電壓關係同[三相變壓器](three-phase-transformer.md)

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.20–26〕
