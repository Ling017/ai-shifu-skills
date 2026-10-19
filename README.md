# AI Shifu Skills

This repository stores AI Shifu related Codex skills.

## Skills

- `ai-shifu-sales-conversion`: sales conversion assistant for AI Shifu leads, follow-up scripts, package guidance, handoff, and customer success.

- [`ai-business-learning-coach`](ai-business-learning-coach/README.md): AI 业务实战学习教练。结合业务项目学习 AI 落地、产品工程与数据知识库判断，支持原课互动和个人补学课。Skill 规则与辅助代码采用 MIT；课程正文及相关材料保留原权利，详见 [授权范围](ai-business-learning-coach/RIGHTS.md)。

- [个性化教学设计](ai-shifu-personalization-designer/README.md)（`ai-shifu-personalization-designer`，3.0.1）：从教师经验与资料中提炼教学判断和方法，再设计具体课程的因材施教。可独立使用，不依赖 MarkdownFlow 或课程平台；支持自然语言总结与按需结构化交接，采用 MIT 许可。

## 基础检查

PR 通过 pre-commit.ci 检查 YAML、JSON、合并冲突标记、大文件和常见文本格式；Markdown 的双空格换行会保留。检查不验证教学效果或内容授权。

本地安装 `pre-commit` 后，可运行 `pre-commit run --all-files`。检查配置位于 [`.pre-commit-config.yaml`](.pre-commit-config.yaml)。
