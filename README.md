# Claude Skills Collection - 专业写作与开发技能包

> 这是一个集成了多种专业能力的 Claude Skills 集合，涵盖内容创作、AI味审校、视觉设计、开发工作流等领域。

## 📦 包含的 Skills

| Skill | 触发关键词 | 核心功能 |
|-------|-----------|---------|
| **vibe-writer** | 写作助手、Vibe Writing、全流程写作 | 总控大脑，全流程自动化写作 |
| **ai-proofreading** | 审校、AI味、人味、润色 | 三遍审校流程，系统化降低AI检测率 |
| **image-generator** | 配图、生成图片 | AI图片生成 + 图床上传 |
| **topic-generator** | 选题、给几个方向 | 基于热点生成差异化选题 |
| **content-converter** | 转X、转微博、转小红书 | 长文转社交媒体内容 |
| **personal-knowledge-search** | 素材、案例 | 搜索个人素材库，提供真实案例 |
| **superpowers** | 开发、调试、TDD、重构 | 专业开发工作流 |

---

## 🎯 快速开始

### 安装方式

```bash
# 克隆到 Claude Skills 目录
cd ~/.claude/skills
git clone https://github.com/ma2ong/claude-skills-collection.git
```

### 使用方法

直接在 Claude Code 中用自然语言描述需求：

```
"帮我审校这篇文章"
"生成一个文章配图"
"给我几个选题方向"
"启动 Vibe Writer，我想写一篇深度文章"
```

---

## 📖 Skills 详解

### 1. vibe-writer - 氛围感写作助手

**功能**：全流程自动化写作，从调研到发布一站式服务。

**特点**：
- 像懂技术的老朋友聊天，平和真诚
- 强制要求真实案例和数据支撑
- 9 步闭环自动化流程
- 混合配图策略（概念图 + 真实截图）

**启动指令**：
```
"启动 Vibe Writer，我想写一篇关于 [主题] 的文章"
```

### 2. ai-proofreading - AI味审校

**功能**：系统化降低 AI 检测率，让内容读起来像真人写的。

**三遍审校流程**：
1. **内容审校**：事实准确性、逻辑清晰性、原创性
2. **风格审校**：去除 6 大类 AI 腔
3. **细节打磨**：句子节奏、段落长度、标点使用

**AI腔识别类型**：
- 套话连篇（"在当今XX飞速发展的时代"）
- 机械句式（"首先...其次...最后..."）
- 书面词汇（"显著"→"很明显"）
- 结构机械（段落长度对称）
- 态度中立（各打五十大板）
- 细节缺失（抽象描述多）

### 3. image-generator - 视觉总监

**功能**：AI 图片生成与图床上传一条龙。

**核心能力**：
- 生成高质量配图提示词
- 支持多种 AI 生图工具
- 自动上传图床，返回 Markdown 链接

### 4. topic-generator - 策划顾问

**功能**：基于需求或热点生成高质量选题方向。

**特点**：
- 差异化角度挖掘
- 多维度评估选题价值
- 标题建议与优化

### 5. content-converter - 分发助手

**功能**：将长文浓缩并改写成社交媒体内容。

**支持平台**：
- X / Twitter
- 微博
- 小红书
- 知乎

**特点**：
- 保留核心观点
- 适配平台风格
- 钩子设计优化

### 6. personal-knowledge-search - 外脑

**功能**：搜索个人素材库，获取真实案例。

**特点**：
- 语义搜索能力
- 案例智能提取
- 风格参考匹配

### 7. superpowers - 专业开发工作流

**功能**：专业的软件开发能力，基于obra/superpowers。

**核心能力**：
- 测试驱动开发（TDD）
- 调试模式
- 代码审查
- 计划执行
- 重构

---

## 🏗️ 架构设计

### 渐进式披露 (Progressive Disclosure)

采用业界最佳实践的渐进式加载策略：

| 层级 | Token 消耗 | 加载时机 |
|------|-----------|---------|
| 元数据层 | ~100 tokens | 始终加载 |
| 指令层 | 3000-5000 tokens | 按需加载 |
| 资源层 | 按需 | 任务触发时 |

**Token 效率提升：75%+**

### 单一职责原则

每个 Skill 只做一件事：
- `writer` 不做 `coder` 的活
- `proofreader` 不做 `designer` 的活
- 通过 Skill 组合实现复杂工作流

### 脚本优于生成

确定性任务写成脚本，不占用 LLM Token：
- 图片上传脚本
- 文件处理脚本
- 格式转换脚本

---

## 📁 文件结构

```
claude-skills-collection/
├── README.md                    # 本文件
├── vibe-writer/                 # 总控写作助手
│   ├── SKILL.md
│   └── references/              # 风格、视觉、工作流规则
├── ai-proofreading/             # AI味审校
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── assets/
├── image-generator/             # 图片配图
│   ├── SKILL.md
│   ├── scripts/
│   └── assets/
├── topic-generator/             # 选题生成
│   └── SKILL.md
├── content-converter/           # 内容转换
│   └── SKILL.md
├── personal-knowledge-search/   # 素材搜索
│   └── SKILL.md
└── superpowers/                 # 开发工作流
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── assets/
```

---

## 🔗 相关资源

- [Anthropic Skills 官方仓库](https://github.com/anthropics/skills)
- [Agent Skills 开放标准](https://agentskills.io)
- [Simon Willison: Skills vs MCP](https://simonwillison.net/2025/Oct/16/claude-skills/)

---

## 📝 更新日志

### v1.0.0 (2026-01-21)

- ✨ 初始版本发布
- 📦 7 个专业 Skills
- 🎯 渐进式披露架构
- 💡 单一职责设计

---

## 📄 许可证

MIT License

---

*让 AI 写作更专业、更高效、更有人味。*
