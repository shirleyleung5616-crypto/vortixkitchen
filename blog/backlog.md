# Vortix Kitchen 博客内容待写清单（Backlog）

> 规则：每篇只写一个痛点，3 min read，英文，问题导向 + 利他思维（帮客户避坑/省钱/不被扣柜）。
> 新增一篇 = 往 `blog/build_blog.py` 的 `ARTICLES` 列表追加一个 dict → 重跑 `python blog/build_blog.py` → 周一自动化部署 + IndexNow。
> 目标：客户在 Google / ChatGPT 搜「痛点 + 怎么解决」时，我们的文章被推荐 → 读 → 发 WhatsApp/邮件询盘。

## 已上线（19 篇）
- **Returns**：pain-dead-on-arrival / pain-cracked-glass / pain-slow-heating
- **Reliability**：pain-igbt-overheat / pain-dusty-fan / pain-voltage-spike / **pain-cooling-fans** / **pain-insect-proof**
- **Customs**：pain-ce-sticker / pain-wrong-plug / pain-no-local-rep / **pain-kazakhstan-eac**（认证类仅保留此 1 篇，其余删除）
- **Buying**：article-induction-vs-infrared / article-product-showcase / article-cookware-magnetism / article-switch-from-gas / **pain-oem-brand** / **pain-safe-payment** / **pain-voltage-frequency**

## 待写池（按主题分组，每周挑 1–2 篇上线）

### A. 清关合规（国家细分）— ⛔ 雪姐 2026-08-27 明确：认证/清关合规类一律不写（无关痛痒、废话），本组取消
- [x] 肯尼亚 KEBS / PVoC（原 pain-kenya-pvoc：2026-08-27 雪姐判定废话，已删除下架）
- [x] 哈萨克斯坦 / 欧亚经济联盟 EAC 认证（TR CU）（已上线：pain-kazakhstan-eac；认证类仅保留此篇）
- 以下取消，不再写：乌兹别克斯坦+东南亚 SNI/SIRIM/TISI、南非 NRCS/SABS、各国插头电压速查表

### B. OEM/ODM 与品牌化
- [ ] 首批 MOQ 怎么定 + 20/40 尺柜能装多少台
- [ ] 贴牌(OEM) vs 自有模具(ODM)：成本与风险对比
- [ ] 生产周期与产能：大单如何排产不拖期

### C. 采购与信任
- [x] 如何安全付给中国工厂（定金比例 / 验厂 / 验货）（已上线：pain-safe-payment）
- [x] ~~出货前验货清单~~（pain-preshipment-check：雪姐判定为废话，已下架删除；DOA 防护改由 pain-dead-on-arrival 正文 + 验货条款覆盖）
- [ ] 备件与售后：进口商如何建自己的备件池

### D. 规格与适配
- [x] 电压/频率适配（全市场 220–240V 50Hz，少数需 110V）（已上线：pain-voltage-frequency）
- [ ] 商用 vs 家用：耐久与保修怎么选
- [ ] 高海拔地区（哈萨克斯坦等）沸点影响与对策
- [ ] 商用电磁炉功率怎么选（按餐厅类型）

### E. 使用与维护 — ⛔ 雪姐 2026-08-27：说明书/操作手册类不吸睛，一律不写，本组取消
- 错误代码 / 一直蜂鸣 排查（说明书类，不写）
- 多尘环境清洁与保养（说明书类，不写）

## 写作计划（6 周，每周一自动化上线；之后循环补充 A–E 剩余项）
- **W1** ✅ pain-oem-brand（已上线）；pain-nigeria-soncap 已删除（2026-08-27 雪姐判定废话）
- **W2** ✅ 电压/频率适配 (pain-voltage-frequency，含 FAQ 结构化数据) — 已上线；pain-kenya-pvoc 已删除（2026-08-27 雪姐判定废话）
- **W3** ✅ 如何安全付款 (pain-safe-payment) + 出货前验货清单（已下架）
- **W3 增补（2026-08-26）** ✅ 可靠性新增 2 篇：pain-cooling-fans（2/4 风扇可按市场定制散热）+ pain-insect-proof（防虫/防蟑螂密封结构）
- **W4**：商用 vs 家用 + 集装箱装载量计算
- **W5**：哈萨克斯坦 EAC + 备件与售后策略
- **W6**：高海拔对策（哈萨克斯坦等，非说明书式、属采购选型痛点）

## 增强被推荐概率（GEO 优化，按周叠加）
1. 每篇加 **FAQ 结构化数据**（抢 Google "People also ask" + ChatGPT 引用）—— W2 起叠加。
2. 内链成簇（related 字段已做，保持每篇 3 条相关链接）。
3. 用 **GSC** 看哪些 query 带来曝光，缺什么补什么（数据驱动扩内容）。
4. llms.txt 随文章增加同步更新（已含 Blog 段）。
