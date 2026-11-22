---
title: 開路與短路測試
en: Open-Circuit and Short-Circuit Tests
aliases: [開路測試, 短路測試, 開路與短路測試, open-circuit test, short-circuit test, OC test, SC test]
chapters: [ch02]
sources: [sources/ch02.md]
updated: 2026-11-23
status: draft
---

# 開路與短路測試（Open-Circuit and Short-Circuit Tests）

## 一句話說明
只做兩個實驗，就能量出變壓器等效電路的所有參數：**開路測試**量激磁支路，**短路測試**量串聯阻抗。

## 白話解釋
- 開路測試：二次側不接東西，所以電流只能走激磁支路——量到的就是激磁支路
- 短路測試：二次側直接短路，只要很低的電壓就有額定電流，激磁支路幾乎沒電流——量到的就是串聯阻抗〔講義 p.24–26〕

## 正式內容
| | 開路測試 | 短路測試 |
|---|---|---|
| 接法 | 一側開路，另一側加**額定電壓** | 低壓側短路，高壓側接可調電壓源，調到**額定電流** |
| 通常在哪一側做 | 低壓側（電壓較低，好量） | 高壓側（電流較小，好量） |
| 電流流經 | 幾乎全部經過激磁支路 | 幾乎全部經過串聯阻抗 |
| 求得 | $R_C$、$X_M$ | $R_{eq}$、$X_{eq}$ |

〔講義 p.24–26〕

**開路測試的計算**〔講義 p.24–25、p.28〕

$$ \text{PF} = \cos\theta = \frac{P_{OC}}{V_{OC}I_{OC}}, \qquad Y_E = \frac{I_{OC}}{V_{OC}}\angle -\cos^{-1}\text{PF} = \frac{1}{R_C} - j\frac{1}{X_M} $$

**短路測試的計算**〔講義 p.26–27〕

$$ \text{PF} = \frac{P_{SC}}{V_{SC}I_{SC}}, \qquad Z_{SE} = \frac{V_{SC}}{I_{SC}}\angle\cos^{-1}\text{PF} = R_{eq} + jX_{eq} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $V_{OC}, I_{OC}, P_{OC}$ | 開路測試量到的電壓、電流、功率 | V、A、W |
| $V_{SC}, I_{SC}, P_{SC}$ | 短路測試量到的電壓、電流、功率 | V、A、W |
| $Y_E$ | 激磁導納（excitation admittance） | S |
| $Z_{SE}$ | 串聯阻抗 | Ω |
| PF | 功率因數 | — |

- 實際變壓器的開路功因一定是落後，所以導納角取負號〔講義 p.25〕
- 求得的值屬於**做測試的那一側**；要畫在同一側的等效電路，需用 $a^2$ 換算〔講義 p.25、p.29〕
- 短路測試時要注意把一次電壓維持在安全範圍，別燒壞繞組〔講義 p.25〕

完整示範見[例 2-2](../examples/ch02-oc-sc-test.md)。

## 和其他概念的關係
- 求的是[變壓器等效電路](transformer-equivalent-circuit.md)的元件
- 功率因數見[交流功率](ac-power.md)
- 同步發電機也用開路、短路測試求參數，見[同步機參數測試](synchronous-machine-tests.md)（Ch.4）

## 出處
- [Ch.2 來源摘要](../sources/ch02.md)〔講義 p.23–29〕
