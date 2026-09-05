# Vortix Kitchen 博客内容待写清单（Backlog）

> 规则：每篇只写一个痛点，3 min read，英文，问题导向 + 利他思维（帮客户避坑/省钱/不被扣柜）。
> 新增一篇 = 往 `blog/build_blog.py` 的 `ARTICLES` 列表追加一个 dict → 重跑 `python blog/build_blog.py` → 周一自动化部署 + IndexNow。
> 目标：客户在 Google / ChatGPT 搜「痛点 + 怎么解决」时，我们的文章被推荐 → 读 → 发 WhatsApp/邮件询盘。

## 已上线（24 篇）
- **Returns**：pain-dead-on-arrival / pain-cracked-glass / pain-slow-heating
- **Reliability**：pain-igbt-overheat / pain-dusty-fan / pain-voltage-spike / **pain-cooling-fans** / **pain-insect-proof**
- **Customs**：pain-ce-sticker / pain-wrong-plug / pain-no-local-rep / **pain-kazakhstan-eac**（认证类仅保留此 1 篇，其余删除）
- **Buying**：article-induction-vs-infrared / article-product-showcase / article-cookware-magnetism / article-switch-from-gas / **pain-oem-brand** / **pain-safe-payment** / **pain-voltage-frequency** / **pain-moq-container-loading** / **pain-oem-vs-odm** / **pain-production-scheduling** / **pain-spare-parts-pool** / **pain-commercial-vs-home** / **pain-high-altitude** / **pain-commercial-power**

## 待写池（按主题分组；2026-09-05 起每日自动化每天 10:00 取第一个未勾选项上线，一天 1 篇）

### A. 清关合规（国家细分）— ⛔ 雪姐 2026-08-27 明确：认证/清关合规类一律不写（无关痛痒、废话），本组取消
- [x] 肯尼亚 KEBS / PVoC（原 pain-kenya-pvoc：2026-08-27 雪姐判定废话，已删除下架）
- [x] 哈萨克斯坦 / 欧亚经济联盟 EAC 认证（TR CU）（已上线：pain-kazakhstan-eac；认证类仅保留此篇）
- 以下取消，不再写：乌兹别克斯坦+东南亚 SNI/SIRIM/TISI、南非 NRCS/SABS、各国插头电压速查表

### B. OEM/ODM 与品牌化
- [x] 首批 MOQ 怎么定 + 20/40 尺柜能装多少台（已上线：pain-moq-container-loading）
- [x] 贴牌(OEM) vs 自有模具(ODM)：成本与风险对比（已上线：pain-oem-vs-odm）
- [x] 生产周期与产能：大单如何排产不拖期（已上线：pain-production-scheduling）

### C. 采购与信任
- [x] 如何安全付给中国工厂（定金比例 / 验厂 / 验货）（已上线：pain-safe-payment）
- [x] ~~出货前验货清单~~（pain-preshipment-check：雪姐判定为废话，已下架删除；DOA 防护改由 pain-dead-on-arrival 正文 + 验货条款覆盖）
- [x] 备件与售后：进口商如何建自己的备件池（已上线：pain-spare-parts-pool）

### D. 规格与适配
- [x] 电压/频率适配（全市场 220–240V 50Hz，少数需 110V）（已上线：pain-voltage-frequency）
- [x] 商用 vs 家用：耐久与保修怎么选（已上线：pain-commercial-vs-home）
- [x] 高海拔地区（哈萨克斯坦等）沸点影响与对策（已上线：pain-high-altitude）
- [x] 商用电磁炉功率怎么选（按餐厅类型）（已上线：pain-commercial-power）
- [ ] 电磁炉 vs 电陶炉：选错炉型的终端退货风险 + 破除"必须换锅"误解（非说明书式、采购选型 P&L 角度，slug 建议：pain-induction-cookware-myth）
  - 素材（雪姐 2026-09-01 提供，写稿时提炼为采购决策钩子，**勿写成使用说明**）：①工作原理=电磁炉磁场直热锅具、玻璃面仅微温；电陶炉先热玻璃陶瓷面板再传锅、关火后余热持续。②体验=烧水 2–3 分钟 vs 5–6 分钟；电磁炉溢出液落低温玻璃可轻松擦、电陶炉高温使残渣焦结难清且易刮花、表面老化快。③清洁=电磁炉可铺纸巾吸油、电陶炉高温无法实现。④锅具=现代锅具多为通用设计，磁铁测锅底即可确认、无需全部更换。

### E. 使用与维护 — ⛔ 雪姐 2026-08-27：说明书/操作手册类不吸睛，一律不写，本组取消
- 错误代码 / 一直蜂鸣 排查（说明书类，不写）
- 多尘环境清洁与保养（说明书类，不写）

### F. ZCode 自拟痛点池（2026-09-05 雪姐授权自拟：利他思维、帮客户解决问题/创造价值；不写说明书、不写认证类）——按下列顺序每天自动取用一条

- [ ] **样品很好、大货拉胯：工厂批量换料怎么防**（slug 建议：pain-bom-substitution）
  - 素材（ZCode 拟，写时提炼为采购防坑钩子）：①钩子=退货高峰总在开卖 2–3 个月后出现，根因常是工厂大货偷换料：铜线圈盘→铝盘、面板玻璃减薄、电源线/插头缩水、风扇降级。②客户 P&L：厂里省 1 美元，赔上的是你的退货率、差评和牌子。③给可抄进合同/PO 的 3 处条款：关键件品牌型号在 BOM 写死、封样（golden sample）双方签封、擅自换料=违约。④到货抽检 3 个快速对照点（整柜称重对 bill of loading、拆一台对照封样、关键件拍照留证）。走采购风控角度，勿写成验货说明书。
- [ ] **便宜 2 美元的炉子为什么让你亏钱：保修成本总账**（slug 建议：pain-warranty-math）
  - 素材（ZCode 拟）：①钩子=故障率 1% 和 5% 的炉子进价只差几十美分，保修成本却差掉一个毛利点。②给算法：保修准备金 = 年销量 × 故障率 ×（换机成本 + 双程运费 + 处理工时）；便宜货真实成本 = 进价 + 运费 + 关税 + 保修金。③给比价表模板：按 TCO 比价而不是按单价比价，可直接抄进内部采购表。④利他落点：帮客户识破"低价陷阱"的算账工具。
- [ ] **集装箱雨：海运霉变毁掉整柜炉子**（slug 建议：pain-container-rain）
  - 素材（ZCode 拟）：①钩子=发东南亚的柜子开门一股霉味：海上昼夜温差让柜内结露滴水（container rain），纸箱软塌、彩盒霉斑、电路板受潮，零售端整批拒收。②向工厂要的防潮包装规格：真空/防潮袋、干燥剂用量与摆放、缠绕膜+柜顶防雨纸、瓦楞箱等级按潮湿市场加码。③装柜前 2 项自查（柜体干燥无破洞、垫木含水）。④可直接写进 PO 的一句话防潮条款模板。走物流风控角度，不是说明书。
- [ ] **错过旺季=资金压一年：炉子采购日历**（slug 建议：pain-season-timing）
  - 素材（ZCode 拟）：①钩子=旺季前两周才下单，生产+海运要 60–90 天，到货已过季，资金和货架一起压一年。②主要市场旺季表：中亚/俄罗斯秋冬婚礼+新年前、印尼/马来斋月前零售高峰、非洲年末节日返乡季。③倒排公式：目标上架日 − 90 天（生产 30–45 + 海运 30–45 + 清点上架 7）= 最晚下单日。④利他落点：年度采购拆 2–3 批错峰下单，既赶旺季又不压库存。
- [ ] **电网不稳的市场：发电机带得动商用炉吗**（slug 建议：pain-generator-power）
  - 素材（ZCode 拟）：①钩子=非洲/中亚不少餐馆靠发电机，电磁炉启动浪涌电流大，发电机容量不足就跳闸，客户以为是炉子坏了——退货+差评。②给选型口诀：发电机额定容量 ×0.8 反推可带炉子总功率；多台炉分时启动、商用大功率机型向工厂要软启动/浪涌参数。③开餐厅/投标前要向工厂问的 2 个参数。④对齐 pain-high-altitude / pain-commercial-power 的选型写法，勿写成操作手册。
- [ ] **零下 30℃ 运输：俄罗斯/中亚冬季到货"死屏"**（slug 建议：pain-cold-climate）
  - 素材（ZCode 拟）：①钩子=冬季海运+陆运进中亚/俄罗斯，到货 LCD 发黑花屏、塑料件脆裂——低温超出电子件额定存储温度，不是质量问题却被当质量投诉。②询价时问工厂的 3 个低温规格：整机存储温度下限、LCD/电容低温等级、彩盒纸箱低温抗脆。③冬季收货流程：先 12–24 小时复温再通电验机，冷开机=批量"假故障"。④可写进采购条款的一句话。采购风险角度，非使用说明。
- [ ] **柜子到了 30 台破损，找谁赔：FOB/CIF 货损责任**（slug 建议：pain-incoterms-damage）
  - 素材（ZCode 拟）：①钩子=运输段货损，进口商找工厂、工厂指条款——风险划分看贸易术语，不懂就吃哑巴亏。②责任分界一句话讲清：FOB=装船后风险归买方；CIF=卖方负责投保但风险同样过船舷，谁投保谁向保险公司索赔；货运险档次覆盖差别。③给行动清单：哪段该买险、破损留证（照片+柜检记录）、向保险公司索赔的时效窗口。④贸易风控角度，不涉及认证/清关。
- [ ] **"口头独家"一钱不值：区域独家经销怎么谈才有用**（slug 建议：pain-exclusivity）
  - 素材（ZCode 拟）：①钩子=业务员口头答应"你独家"，半年后同款出现在隔壁进口商的货架，价格战打在自己地盘。②工厂愿意给独家的真实条件：首单量门槛、年采购量承诺、品牌/市场投入分摊。③合同必须写死 4 条：独家品类与型号清单、territory 边界、违约赔偿、期限与续约条件。④利他落点：独家是买来的护城河，不是聊出来的。
- [ ] **帮你的零售客户算账：电磁炉 vs 液化气使用成本**（slug 建议：pain-induction-vs-lpg-cost）
  - 素材（ZCode 拟）：①钩子=非洲/东南亚液化气涨价换气难，终端用户算不清账就不换炉——进口商的货趴在仓库。②给进口商一套终端算账模板：代入当地电价/气价、热效率对比（电磁 ~85% vs 燃气 ~45%）、月燃料费对比公式，不写具体国家价格。③用法：印成零售小卡片或 WhatsApp 图，帮下游零售动销。④利他落点：你的货好卖，补货才会快。

（写作顺序=上面列表顺序，每日一篇；雪姐如觉得某条不该写，按老规矩标 [x] 注明取消即可，自动化会自动跳过。）

## 写作计划（6 周，每周一自动化上线；之后循环补充 A–E 剩余项）
- **W1** ✅ pain-oem-brand（已上线）；pain-nigeria-soncap 已删除（2026-08-27 雪姐判定废话）
- **W2** ✅ 电压/频率适配 (pain-voltage-frequency，含 FAQ 结构化数据) — 已上线；pain-kenya-pvoc 已删除（2026-08-27 雪姐判定废话）
- **W3** ✅ 如何安全付款 (pain-safe-payment) + 出货前验货清单（已下架）
- **W3 增补（2026-08-26）** ✅ 可靠性新增 2 篇：pain-cooling-fans（2/4 风扇可按市场定制散热）+ pain-insect-proof（防虫/防蟑螂密封结构）
- **W4**：商用 vs 家用 + 集装箱装载量计算
- **W5**：✅ pain-kazakhstan-eac + ✅ pain-spare-parts-pool（备件与售后）
- **W6**：✅ 高海拔对策（哈萨克斯坦等，非说明书式、属采购选型痛点）（已上线：pain-high-altitude）

## 增强被推荐概率（GEO 优化，按周叠加）
1. 每篇加 **FAQ 结构化数据**（抢 Google "People also ask" + ChatGPT 引用）—— W2 起叠加。
2. 内链成簇（related 字段已做，保持每篇 3 条相关链接）。
3. 用 **GSC** 看哪些 query 带来曝光，缺什么补什么（数据驱动扩内容）。
4. llms.txt 随文章增加同步更新（已含 Blog 段）。
