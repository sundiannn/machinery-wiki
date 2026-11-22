---
title: 速度調整率
en: Speed Regulation
aliases: [速度調整率, SR, speed regulation]
chapters: [ch03, ch05]
sources: [sources/ch03.md, sources/ch05.md]
updated: 2026-11-23
status: draft
---

# 速度調整率（Speed Regulation）

## 一句話說明
電動機加上負載後轉速會掉多少——速度調整率越小，轉速越穩定。

## 白話解釋
電扇加上阻力（例如被手擋住）會轉慢一點；速度調整率就是在量「從沒負載到滿載，轉速掉了百分之幾」〔比喻〕〔AI 補充〕。

## 正式內容
〔講義 p.33〕

$$ \text{SR} = \frac{n_{nl} - n_{fl}}{n_{fl}}\times100\% = \frac{\omega_{nl} - \omega_{fl}}{\omega_{fl}}\times100\% $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $n_{nl}, n_{fl}$ | 無載、滿載轉速 | rpm |
| $\omega_{nl}, \omega_{fl}$ | 無載、滿載角速度 | rad/s |

- 衡量電動機在負載變化時維持轉速的能力，也粗略反映轉矩－轉速特性曲線的形狀〔講義 p.33〕
- SR 為正：負載增加時轉速下降；SR 為負：負載增加時轉速上升〔講義 p.33〕
- SR 的大小約略代表轉矩－轉速曲線的斜率有多陡〔講義 p.33〕

**例：同步電動機**〔講義 Ch.5 p.6〕
- 同步電動機從無載到脫出轉矩轉速都固定，速度調整率為 0%，見[同步電動機的轉矩與負載](synchronous-motor-torque-speed.md)

## 和其他概念的關係
- 發電機對應的指標是電壓調整率，見[電壓調整率與效率](voltage-regulation-and-efficiency.md)
- 屬於[交流電機](ac-machines.md)一章

## 出處
- [Ch.3 來源摘要](../sources/ch03.md)〔講義 p.33〕
- [Ch.5 來源摘要](../sources/ch05.md)〔講義 Ch.5 p.6〕
