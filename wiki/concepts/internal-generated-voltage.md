---
title: 內生電壓
en: Internal Generated Voltage
aliases: [內生電壓, 內部感應電壓, E_A, 開路特性, OCC, internal generated voltage]
chapters: [ch04]
sources: [sources/ch04.md]
updated: 2026-11-23
status: draft
---

# 內生電壓（Internal Generated Voltage）

## 一句話說明
同步發電機每相內部產生的電壓 $E_A = K\phi\omega$：磁通越強、轉得越快，電壓越大；而磁通由轉子的場電流控制。

## 白話解釋
$E_A$ 就是發電機「肚子裡」產生的電壓。轉速通常必須固定（才能維持頻率），所以實際上調整 $E_A$ 的旋鈕只有一個：轉子的場電流〔講義 p.2、p.22〕〔AI 補充〕。

## 正式內容
- 由 Ch.3 的 $E_A = \sqrt2\pi N_C\phi f$ 出發，電壓取決於磁通、頻率（轉速）與構造〔講義 p.2〕
- 改寫成強調「運轉中會變的量」的形式〔講義 p.2〕：

$$ E_A = K\phi\omega $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $E_A$ | 每相內生電壓 | V |
| $K$ | 代表電機構造的常數 | — |
| $\phi$ | 磁通 | Wb |
| $\omega$ | 角速度 | rad/s |

- $\omega$ 用**電**弧度每秒表示時，$K = N_C/\sqrt2$〔講義 p.2〕
- $\omega$ 用**機械**弧度每秒表示時，$K = N_CP/(\sqrt2\cdot2)$〔講義手寫補充 p.2〕（講義印刷的 $N_CP/\sqrt2$ 已被老師劃掉更正）
- $E_A$ 正比於磁通與轉速，而磁通又取決於轉子**場電流** $I_F$；$E_A$ 對 $I_F$ 的曲線稱為**磁化曲線**或**開路特性（open-circuit characteristic, OCC）**〔講義 p.2〕

## 和其他概念的關係
- 來自[交流電機的感應電壓](ac-induced-voltage.md)
- OCC 的形狀和[磁化曲線](magnetization-curve.md)一樣會飽和；量測方法見[同步機參數測試](synchronous-machine-tests.md)
- 是[同步機等效電路](synchronous-equivalent-circuit.md)中的電壓源
- 屬於[同步發電機](synchronous-generator.md)一章

## 出處
- [Ch.4 來源摘要](../sources/ch04.md)〔講義 p.2〕
