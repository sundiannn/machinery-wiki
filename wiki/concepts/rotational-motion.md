---
title: 旋轉運動
en: Rotational Motion
aliases: [旋轉運動, 轉矩, 力矩, 角速度, torque, angular velocity]
chapters: [ch01]
sources: [sources/ch01.md]
updated: 2026-11-23
status: draft
---

# 旋轉運動（Rotational Motion）

## 一句話說明
電機都在「轉」，所以要用角度、角速度、轉矩來描述它，對應直線運動的距離、速度、力。

## 白話解釋
轉矩就是「扭力」：用扳手轉螺絲時，力越大、手握得離螺絲越遠，就越容易轉動〔比喻〕〔AI 補充〕。

## 正式內容
直線運動與旋轉運動的對照〔講義 p.2–5〕：

| 直線運動 | 旋轉運動 |
|---|---|
| 位置 $r$ | 角位置 $\theta$ |
| 速度 $v = dr/dt$ | 角速度 $\omega = d\theta/dt$（逆時針為正） |
| 加速度 $a = dv/dt$ | 角加速度 $\alpha = d\omega/dt$ |
| 力 $F$ | 轉矩 $\tau$ |
| 牛頓定律 $F = ma$ | 牛頓旋轉定律 $\tau = J\alpha$ |
| 功 $W = Fr$ | 功 $W = \tau\theta$ |
| 功率 $P = Fv$ | 功率 $P = \tau\omega$ |

**轉速的三種單位**〔講義 p.2〕

$$ n_m = 60 f_m, \qquad f_m = \frac{\omega_m}{2\pi} $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\omega_m$ | 機械角速度 | rad/s |
| $f_m$ | 每秒轉數 | rps |
| $n_m$ | 每分鐘轉數 | rpm |

下標 $m$ 代表「機械量」，用來和電氣量區分〔講義 p.2〕。

**轉矩**：施力和「力的作用線到轉軸的最短距離」的乘積〔講義 p.3–4〕

$$ \tau = rF\sin\theta $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $\tau$ | 轉矩 | N·m |
| $r$ | 轉軸到施力點的距離 | m |
| $F$ | 施力 | N |
| $\theta$ | $\mathbf{r}$ 與 $\mathbf{F}$ 的夾角 | ° |

若力的作用線通過轉軸，轉矩為零〔講義 p.3〕。

**牛頓旋轉定律**〔講義 p.4–5〕

$$ \tau = J\alpha $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $J$ | 轉動慣量（moment of inertia），相當於直線運動的質量 | kg·m² |
| $\alpha$ | 角加速度 | rad/s² |

**功率**〔講義 p.5〕

$$ P = \tau\omega $$

| 符號 | 意義 | 單位 |
|---|---|---|
| $P$ | 功率 | W |
| $\omega$ | 角速度（必須用 rad/s） | rad/s |

## 和其他概念的關係
- 電機的機械側都用這些量描述，見[電機](electric-machines.md)
- [線性直流機](linear-dc-machine.md)的 $P = Fv$ 對應到真實旋轉電機的 $P = \tau\omega$
- 交流電機的轉換功率 $P_{conv} = \tau_{ind}\omega_m$，見[電機損失與功率流](machine-losses-and-power-flow.md)

## 常見誤解
- $P = \tau\omega$ 只有在功率用 W、轉矩用 N·m、轉速用 **rad/s** 時才成立，用 rpm 代入會錯〔講義 p.5〕

## 出處
- [Ch.1 來源摘要](../sources/ch01.md)〔講義 p.1–5〕
