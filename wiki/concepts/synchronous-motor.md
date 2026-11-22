---
title: 同步電動機
en: Synchronous Motor
aliases: [同步電動機, 同步馬達, synchronous motor, 同步機]
chapters: [ch05]
sources: [sources/ch05.md]
updated: 2026-11-23
status: draft
---

# 同步電動機（Synchronous Motor）

## 一句話說明
把同步發電機「反過來用」就是同步電動機：定子通三相電產生旋轉磁場，轉子電磁鐵被它拉著，以完全相同的速度旋轉。

## 白話解釋
想像用一根橡皮筋拉著玩具車繞圈：手（定子旋轉磁場）在前面跑，車子（轉子）在後面以同樣速度跟著，兩者之間的橡皮筋被拉開一個角度。負載越重，橡皮筋拉得越開，但車速不變〔比喻〕〔AI 補充〕。

## 正式內容
**基本原理**〔講義 p.1–2〕
- 轉子場電流 $I_F$ 產生穩定的磁場 $\mathbf{B}_R$；定子接三相電壓，三相電流產生均勻的旋轉磁場 $\mathbf{B}_S$
- 兩個磁場同時存在，轉子磁場會像兩根條形磁鐵一樣想和定子磁場對齊；定子磁場在轉，轉子就一直追
- 兩磁場夾角越大（到某個最大值為止），轉子受的轉矩越大
- 同步電動機的基本原理：轉子「追著」旋轉的定子磁場繞圈，**永遠追不上**
- 同步電動機和同步發電機是**同一台實體機器**，Ch.3、Ch.4 的轉速、功率、轉矩公式全部適用

**等效電路**〔講義 p.2〕
電樞電流 $\mathbf{I}_A$ 的參考方向改為**流入**電機，所以 KVL 變成：

$$ \mathbf{V}_\phi = \mathbf{E}_A + jX_S\mathbf{I}_A + R_A\mathbf{I}_A \quad\Longleftrightarrow\quad \mathbf{E}_A = \mathbf{V}_\phi - jX_S\mathbf{I}_A - R_A\mathbf{I}_A $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\mathbf{V}_\phi$ | 每相端電壓（由電源決定） | V |
| $\mathbf{E}_A$ | 內生電壓 | V |
| $\mathbf{I}_A$ | 電樞電流（流入電機為正） | A |

**從磁場看：發電機怎麼變成電動機**〔講義 p.3–5〕
- 發電機：原動機推著轉子，$\mathbf{B}_R$ 領先 $\mathbf{B}_{net}$，感應轉矩與運動方向**相反**（反轉矩）
- 若原動機突然失去動力、反而拖住轉軸 → 轉子減速，$\mathbf{B}_R$ 落後 $\mathbf{B}_{net}$ → 由 $\tau = k\mathbf{B}_R\times\mathbf{B}_{net}$，轉矩方向反轉、變成和運動方向**相同** → 這台機器變成電動機
- 轉矩角增大，轉矩跟著增大，直到等於負載轉矩，再次以同步轉速穩定運轉

| | 發電機 | 電動機 |
|---|---|---|
| $\mathbf{E}_A$ 與 $\mathbf{V}_\phi$ | $\mathbf{E}_A$ **領先** $\mathbf{V}_\phi$ | $\mathbf{E}_A$ **落後** $\mathbf{V}_\phi$ |
| $\mathbf{B}_R$ 與 $\mathbf{B}_{net}$ | $\mathbf{B}_R$ 領先 | $\mathbf{B}_R$ 落後 |
| 感應轉矩 | 與運動方向相反（反轉矩） | 與運動方向相同 |

〔講義 p.5〕

**實功率與虛功率的四種組合**〔講義 p.27–28〕
- 同步電機可以供給或吸收實功率 $P$，也可以供給或吸收虛功率 $Q$，四種組合都可能
- 供給 $P$（發電機）：$\mathbf{E}_A$ 領先 $\mathbf{V}_\phi$；吸收 $P$（電動機）：$\mathbf{E}_A$ 落後 $\mathbf{V}_\phi$
- 不論發電機或電動機：$E_A\cos\delta > V_\phi$ 時**供給** $Q$，$E_A\cos\delta < V_\phi$ 時**吸收** $Q$

## 本章地圖
1. 加負載會怎樣、最多能拖多重：[同步電動機的轉矩與負載](synchronous-motor-torque-speed.md)
2. 調場電流會怎樣：[V 曲線](v-curve.md)
3. 調場電流的實際用途：[功率因數校正](power-factor-correction.md)
4. 怎麼讓它轉起來：[同步電動機的啟動](synchronous-motor-starting.md)

## 和其他概念的關係
- 和[同步發電機](synchronous-generator.md)是同一台機器，等效電路見[同步機等效電路](synchronous-equivalent-circuit.md)
- 被拉著轉的原理是[旋轉磁場](rotating-magnetic-field.md)與[交流電機的感應轉矩](ac-induced-torque.md)
- 屬於[交流電機](ac-machines.md)中的同步電機；是[磁場四大原理](four-magnetic-principles.md)「電動機作用」的應用

## 出處
- [Ch.5 來源摘要](../sources/ch05.md)〔講義 p.1–5、p.27–28〕
