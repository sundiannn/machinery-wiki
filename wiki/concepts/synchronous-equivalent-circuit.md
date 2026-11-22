---
title: 同步機等效電路
en: Synchronous Machine Equivalent Circuit
aliases: [同步機等效電路, 電樞反應, 同步電抗, 轉矩角, 同步發電機相量圖, armature reaction, synchronous reactance, torque angle]
chapters: [ch04]
sources: [sources/ch04.md]
updated: 2026-11-23
status: draft
---

# 同步機等效電路（Synchronous Machine Equivalent Circuit）

## 一句話說明
每一相都可以畫成「內生電壓 $E_A$ 串聯一個同步電抗 $X_S$ 和電樞電阻 $R_A$」，輸出端電壓 $V_\phi$ 就是 $E_A$ 扣掉這兩個壓降。

## 白話解釋
發電機內部「想」輸出 $E_A$，但一有電流流出，定子電流自己產生的磁場會干擾原本的磁場（電樞反應），再加上線圈本身的電感與電阻，輸出到外面的電壓 $V_\phi$ 就和 $E_A$ 不一樣了〔講義 p.3–6〕〔AI 補充〕。

## 正式內容
**造成 $E_A$ 與 $V_\phi$ 不同的四個因素**〔講義 p.3〕
1. **電樞反應（armature reaction）**：定子電流扭曲氣隙磁場——通常是影響最大的一項
2. 電樞線圈的自感
3. 電樞線圈的電阻
4. 凸極轉子形狀的影響（本章忽略，只稍微不準確）

**電樞反應**〔講義 p.3–6〕
- 無載時沒有電樞電流，$E_A = V_\phi$
- 接上（落後）負載後，定子電流產生自己的磁場 $\mathbf{B}_S$，並在定子感應出電壓 $\mathbf{E}_{stat}$
- 相電壓是兩者之和 $\mathbf{V}_\phi = \mathbf{E}_A + \mathbf{E}_{stat}$；淨磁場 $\mathbf{B}_{net} = \mathbf{B}_R + \mathbf{B}_S$，和 $\mathbf{V}_\phi$ 同方向
- $\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ 的夾角稱為**內角**或**轉矩角** $\delta$，和發電機送出的功率成正比
- $\mathbf{E}_{stat}$ 落後電流 $\mathbf{I}_A$ 90°、大小正比於 $I_A$，所以 $\mathbf{E}_{stat} = -jX\mathbf{I}_A$，可以用一個串聯電感表示

**同步電抗與每相電壓方程式**〔講義 p.6–7〕

$$ X_S = X + X_A, \qquad \mathbf{V}_\phi = \mathbf{E}_A - jX_S\mathbf{I}_A - R_A\mathbf{I}_A $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $X$ | 電樞反應電抗 | Ω |
| $X_A$ | 定子自感的電抗 | Ω |
| $X_S$ | 同步電抗（synchronous reactance） | Ω |
| $R_A$ | 電樞（定子）電阻 | Ω |
| $\mathbf{V}_\phi$ | 每相端電壓 | V |
| $\mathbf{I}_A$ | 電樞電流 | A |

**完整等效電路**〔講義 p.7–8〕
- 轉子場電路：直流電源供電，以線圈電感與電阻 $R_F$ 串聯表示，另串一個可調電阻 $R_{adj}$ 控制場電流
- 三相各有一個 $E_A$ 串聯 $jX_S$ 與 $R_A$，彼此相差 120°，其餘完全相同；可接成 Y 或 Δ
- Y 接：$V_T = V_L = \sqrt3V_\phi$；Δ 接：$V_T = V_\phi$
- 使用**每相等效電路**時要記得：只有三相負載**平衡**時，三相的電壓電流才相同

**相量圖**〔講義 p.9–10〕
- 以 $\mathbf{V}_\phi$ 為 0° 參考，$\mathbf{E}_A$ 與 $\mathbf{V}_\phi$ 相差電阻壓降與電感壓降
- 相同的 $V_\phi$ 與 $I_A$ 下，**落後負載需要的 $E_A$ 比超前負載大** → 落後負載需要較大的場電流才能維持相同端電壓；$\omega$ 必須固定以維持頻率

## 和其他概念的關係
- $E_A$ 見[內生電壓](internal-generated-voltage.md)；$X_S$、$R_A$ 的量法見[同步機參數測試](synchronous-machine-tests.md)
- 結構和[變壓器等效電路](transformer-equivalent-circuit.md)類似：理想電壓源＋串聯阻抗
- 轉矩角 $\delta$ 決定功率，見[同步機的功率與轉矩](synchronous-power-and-torque.md)
- 磁場的向量相加見[交流電機的感應轉矩](ac-induced-torque.md)
- 當電動機使用時，$\mathbf{I}_A$ 的參考方向改為流入，方程式變成 $\mathbf{V}_\phi = \mathbf{E}_A + jX_S\mathbf{I}_A + R_A\mathbf{I}_A$，見[同步電動機](synchronous-motor.md)
- 屬於[同步發電機](synchronous-generator.md)一章

## 出處
- [Ch.4 來源摘要](../sources/ch04.md)〔講義 p.3–10〕
