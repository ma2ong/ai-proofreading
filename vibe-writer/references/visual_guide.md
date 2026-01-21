# Vibe Writer 视觉指南 (The Look)

本指南定义了配图的审美标准。我们追求**真实感与设计感的平衡**。

## 核心策略：混合配图 (Hybrid Visuals)

一篇文章应包含以下三种类型的图片：

1.  **封面图 (The Vibe)**：极简科技风，设定基调。
2.  **实证图 (The Proof)**：真实的产品截图、代码片段、操作界面。
3.  **解释图 (The Logic)**：Mermaid 流程图或架构图。

## 1. 封面与概念图 (Baoyu Style)

**风格**：Minimalist Tech (极简科技)。
**关键词**：Abstract, Minimalist, Gradient, Tech, Blue/White/Clean.

**提示词公式**：
`[主题抽象] + minimalist style, soft lighting, clean background, high quality, 8k --ar 16:9`

## 2. 真实案例图 (The Real Stuff)

**这是建立信任的关键。**

-   **产品介绍时**：必须使用（或要求用户提供）产品官网截图、发布会 Keynote 截图。
-   **代码演示时**：使用 Carbon 风格的代码截图，或者 IDE 的真实界面截图。
-   **场景描述时**：使用 Unsplash 的高质量实拍图（如程序员桌面、白板讨论）。

**Unsplash 搜索关键词建议**：
- `developer desk setup`
- `whiteboard meeting`
- `coding screen`
- `product launch presentation`

## 3. 生图工具调用 (Nano Banana / Free AI)

在生成配图时，优先调用免费生图工具（如 Nano Banana, Flux, 或其他可用工具）：

-   **首选**：**Nano Banana** (如果可用)。生成速度快，适合迭代。
-   **备选**：Flux, Stable Diffusion, Bing Image Creator (DALL-E 3).
-   **Skill 调用**：使用 `image-generator` skill 来生成提示词或直接调用生图 API (如果配置了)。

**调用指令示例**：
> "使用 image-generator 为本文生成一张封面图，关键词：Agentic AI, minimalist, blue network connection。请尝试调用 Nano Banana 或其他免费工具生成。"

## 配图输出规范

文章中必须插入图片占位符或 Markdown 链接：

```markdown
![封面图](https://images.unsplash.com/photo-xxx)
*(图片来源：Unsplash - Tech Vibe)*

...正文...

![产品界面](https://example.com/product_screenshot.png)
*(图：Claude Code 的真实交互界面，注意看右侧的 Terminal)*
```

---
*Reference: Inspired by Baoyu.io & Apple Design Style*
