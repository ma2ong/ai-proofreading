# Vibe Writer 自动化工作流 (The Logic)

本指南基于 MapleShaw 的自动化写作 Agent 逻辑，定义了从选题到发布的完整生命周期。

## 核心原则 (Prime Directives)

1.  **绝不直接写**：收到主题后，必须先进行调研和选题策划。
2.  **绝不编造**：所有数据、案例必须基于搜索或知识库。
3.  **Think Aloud**：每一步都要输出思考过程。
4.  **版本控制**：初稿 -> 审校版 -> 最终版。

## 标准工作流 (The 9-Step Flow)

### Step 1: 需求分析 & Brief
- 理解用户意图。
- 确定：主题、受众、风格、长度。
- 输出：Brief 文档。

### Step 2: 深度调研 (Research)
- 调用搜索工具 (Tavily/Exa/Google)。
- 查找：最新热点、行业数据、技术细节、反直觉观点。
- 沉淀：关键事实列表。

### Step 3: 选题策划 (Ideation)
- 基于调研，生成 3-4 个差异化选题。
- 每个选题包含：标题、核心角度（Hook）、大纲预览。
- **等待用户确认**。

### Step 4: 风格对齐 (Alignment)
- 加载 `style_guide.md`。
- 确认语调：硅谷极客风 / Vibe Coding 风。

### Step 5: 初稿创作 (Drafting)
- 按照确认的大纲写作。
- 强开头（Hook）。
- 逻辑推进。
- 输出：`draft_v1.md`。

### Step 6: AI味审校 (Anti-AI Review)
- 加载 `anti_ai_checklist.md`。
- 第一遍：逻辑与事实检查。
- 第二遍：去 AI 味（删套话、拆长句）。
- 第三遍：润色与节奏。
- 输出：`draft_v2.md`。

### Step 7: 视觉增强 (Visuals)
- 加载 `visual_guide.md`。
- 为文章生成：1张封面图 + 2-3张配图的提示词。
- 尝试搜索 Unsplash 替代图。
- 插入 Mermaid 图表（如果涉及流程/架构）。

### Step 8: 社媒分发 (Distribution)
- 生成 X/Twitter 版本的 Thread。
- 生成小红书版本的笔记文案。

### Step 9: 最终交付 (Final Polish)
- 输出最终 Markdown 文件。
- 包含所有资源链接。

---
*Reference: Inspired by MapleShaw's Auto Writing Agent*
