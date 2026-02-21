<div align="center">

# 你好，我是Xinyu Liu(Jeff) 👋

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+SC&weight=500&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&random=false&width=600&lines=%E4%B8%80%E5%90%8D%E5%A4%A7%E6%A8%A1%E5%9E%8B%E7%AE%97%E6%B3%95%E5%B7%A5%E7%A8%8B%E5%B8%88;AI+%E5%A4%A7%E8%88%AA%E6%B5%B7%E6%97%B6%E4%BB%A3%E7%9A%84%E6%A8%A1%E5%9E%8B%E8%90%BD%E5%9C%B0%E5%AE%9E%E8%B7%B5%E8%80%85" alt="Typing SVG" />

**把"看起来也许能用"的模型，打磨成可以运转的系统**

<a href="mailto:lxinyujeff@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"/>
</a>
<a href="https://www.linkedin.com/in/lxinyujeff/">
  <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/>
</a>

<img src="https://komarev.com/ghpvc/?username=Bluesmmm&style=flat-square&color=blue" alt="Profile views"/>

</div>

---

### 🎯 当前专注

<div align="center">

`🤖 业务驱动的模型和系统设计` `🐍 训练与对齐策略的稳定落地` `📊 下一代Agent系统的实现` `🔬 面向上线的评测与迭代机制`

</div>

---

### 🛠️ 技术栈

#### 🧠 训练 & 对齐

<p>
<img src="https://skillicons.dev/icons?i=pytorch,python"/>
<img src="https://img.shields.io/badge/Transformers-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black"/>
<img src="https://img.shields.io/badge/DeepSpeed-00A8FF?style=for-the-badge&logo=microsoft&logoColor=white"/>
<img src="https://img.shields.io/badge/FSDP-FF6B6B?style=for-the-badge&logo=meta&logoColor=white"/>
<img src="https://img.shields.io/badge/Megatron--LM-9D4EDD?style=for-the-badge"/>
<img src="https://img.shields.io/badge/PEFT-LoRA-4CC9F0?style=for-the-badge"/>
<img src="https://img.shields.io/badge/TRL-RLHF-F72585?style=for-the-badge"/>
<img src="https://img.shields.io/badge/VeRL-7209B7?style=for-the-badge"/>
</p>

- 落地 SFT/PEFT 训练流水线：熟悉 CPT/Mid-Training/LoRA 及变种方法，覆盖数据迭代、可复现性、超参搜索与收敛控制
- 推进偏好对齐从离线到线上闭环：熟悉 PPO/DPO/GRPO 及变种算法原理，对评测门禁、灰度发布、线上反馈迭代有实操经验
- 优化分布式训练吞吐与显存效率：掌握 Ray/DeepSpeed/Megatron-LM 框架核心机制，以及多机多卡并行与显存策略调优方法

#### ⚡ 推理加速 & 服务化

<p>
<img src="https://skillicons.dev/icons?i=docker,kubernetes,redis,kafka,fastapi"/>
<img src="https://img.shields.io/badge/vLLM-00F5D4?style=for-the-badge"/>
<img src="https://img.shields.io/badge/SGLang-9B5DE5?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Triton-76B900?style=for-the-badge&logo=nvidia&logoColor=white"/>
<img src="https://img.shields.io/badge/Ray_Serve-00CFFF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/AWQ_GPTQ-FF9F1C?style=for-the-badge"/>
</p>

- 应用 vLLM/SGLang 推理链路：熟悉 Continuous Batching、调度队列等机制，能围绕 P99 延迟、QPS 与成本做压测性能调优
- 优化显存与吞吐：熟悉显存占用结构，能通过Cache策略与并发治理等方法避免常见风险，理解量化在效果与性能之间的取舍
- 工程化与可用性设计：具备线上服务治理经验，覆盖超时、重试与回退策略，能够用指标与回归验证支撑灰度发布与稳定迭代

#### 🔍 RAG / Agent

<p>
<img src="https://skillicons.dev/icons?i=elasticsearch"/>
<img src="https://img.shields.io/badge/LangChain-1F2937?style=for-the-badge&logo=langchain&logoColor=white"/>
<img src="https://img.shields.io/badge/Milvus-00A1EA?style=for-the-badge&logo=milvus&logoColor=white"/>
<img src="https://img.shields.io/badge/Reranker-E63946?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Function_Calling-3A86FF?style=for-the-badge"/>
<img src="https://img.shields.io/badge/JSON_Schema-8338EC?style=for-badge&logo=json&logoColor=white"/>
</p>

- 落地 Agentic RAG：实现 Agentic Loop，在证据不足时触发扩检、改写与多跳分解，引用答案阈值降低幻觉、提升可解释性
- 路由与混合检索：按意图、领域进行路由，结合向量召回提升召回鲁棒性，采用检索和重排序，用缓存与元数据约束控制噪声
- 图检索与可追溯证据链：完成实体关系抽取与路径检索、子图摘要，证据可追溯至具体文档/段落，支持问题定位和快速回滚

#### 📊 评测 & 迭代

<p>
<img src="https://skillicons.dev/icons?i=prometheus,grafana,docker,kubernetes,githubactions"/>
<img src="https://img.shields.io/badge/W&B-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black"/>
<img src="https://img.shields.io/badge/Parquet-374151?style=for-the-badge&logo=apacheparquet&logoColor=white"/>
</p>

- 建立评测与质量监控：根据业务指标搭建评测流水线，维护回归集并做分桶分析，支持 A/B 测试并设立阈值确保模型质量可控
- 构建观测与成本治理：搭建 Prometheus/Grafana 指标告警体系，覆盖延迟、QPS、缓存命中等关键指标，形成评估优化闭环
- 回归管控与发布策略：实现数据配置版本化、变更可审计与实验可复现，并通过灰度发布、对照实验与快速回滚降低迭代风险

---

### 📝 博客

<div align="center">

**✨ 敬请期待 ✨**

</div>

### 🔥 连续贡献

<div align="center">

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Bluesmmm&theme=default&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="GitHub Streak"/>

</div>

---
